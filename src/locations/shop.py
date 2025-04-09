from items.item_database import get_item, get_items_by_type, get_items_by_rarity

class Shop:
    """Represents a shop where players can buy and sell items."""
    
    def __init__(self, shop_id, name, description, inventory=None, discount_rate=0, markup_rate=0.2):
        self.id = shop_id
        self.name = name
        self.description = description
        self.inventory = inventory or []
        self.discount_rate = discount_rate  # Percentage discount on prices (0.0 to 1.0)
        self.markup_rate = markup_rate  # Percentage markup on selling prices (0.0 to 1.0)
        
    def add_item(self, item, quantity=1):
        """Add an item to the shop inventory."""
        for i in range(quantity):
            self.inventory.append(item)
            
    def remove_item(self, item):
        """Remove an item from shop inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
        
    def get_buy_price(self, item, player_charm=0):
        """Calculate the buying price for an item, factoring in charm and discount."""
        base_price = item.get_value()
        charm_discount = min(0.25, player_charm * 0.02)  # Max 25% discount from charm
        final_discount = self.discount_rate + charm_discount
        
        return max(1, int(base_price * (1 - final_discount)))
        
    def get_sell_price(self, item, player_charm=0):
        """Calculate the selling price for an item, factoring in charm and markup."""
        base_price = item.get_value()
        charm_bonus = min(0.15, player_charm * 0.01)  # Max 15% bonus from charm
        final_sell_rate = 0.5 - self.markup_rate + charm_bonus  # Base sell rate is 50% of value
        
        return max(1, int(base_price * final_sell_rate))
        
    def buy_item(self, game_state, item):
        """Player buys an item from the shop."""
        player = game_state.player
        price = self.get_buy_price(item, player.charm)
        
        # Check if player has enough credits
        if player.credits < price:
            return False, "Not enough credits."
            
        # Remove item from shop
        if not self.remove_item(item):
            return False, "Item not available."
            
        # Add to player inventory and deduct credits
        game_state.add_to_inventory(item)
        player.credits -= price
        
        return True, f"Purchased {item.name} for {price} credits."
        
    def sell_item(self, game_state, item):
        """Player sells an item to the shop."""
        player = game_state.player
        price = self.get_sell_price(item, player.charm)
        
        # Remove from player inventory
        if item not in game_state.inventory:
            return False, "You don't have this item."
            
        game_state.remove_from_inventory(item)
        
        # Add to shop and give credits
        self.add_item(item)
        player.credits += price
        
        return True, f"Sold {item.name} for {price} credits."
        
class ShopManager:
    """Manages all shops in the game."""
    
    def __init__(self, game_state, ui):
        self.game_state = game_state
        self.ui = ui
        self.shops = {}
        
    def add_shop(self, shop):
        """Register a shop in the manager."""
        self.shops[shop.id] = shop
        
    def get_shop(self, shop_id):
        """Get a shop by ID."""
        return self.shops.get(shop_id)
        
    def open_shop_interface(self, shop_id):
        """Open the shop interface for a specific shop."""
        shop = self.get_shop(shop_id)
        if not shop:
            self.ui.display_message("Shop not found.")
            return
            
        self.game_state.shop_open = True
        player = self.game_state.player
        
        while self.game_state.shop_open:
            self.ui.clear_screen()
            self.ui.display_message(f"Welcome to {shop.name}!")
            self.ui.display_message(shop.description)
            self.ui.display_message(f"Your credits: {player.credits}")
            
            options = ["Buy Items", "Sell Items", "Exit Shop"]
            choice = self.ui.get_choice("What would you like to do?", options)
            
            if choice == 0:  # Buy
                self._handle_buying(shop)
            elif choice == 1:  # Sell
                self._handle_selling(shop)
            else:  # Exit
                self.game_state.shop_open = False
                self.ui.display_message("Thank you for your business!")
                
    def _handle_buying(self, shop):
        """Handle the buying interface."""
        if not shop.inventory:
            self.ui.display_message("The shop has no items available.")
            return
            
        self.ui.clear_screen()
        self.ui.display_message(f"Available Items at {shop.name}")
        self.ui.display_message(f"Your credits: {self.game_state.player.credits}")
        
        # Display all items for sale
        options = []
        items = []
        
        for item in shop.inventory:
            price = shop.get_buy_price(item, self.game_state.player.charm)
            options.append(f"{item.name} - {price} credits - {item.description}")
            items.append(item)
            
        options.append("Back")
        
        choice = self.ui.get_choice("Select an item to buy:", options)
        
        if choice < len(items):  # Selected an item
            selected_item = items[choice]
            success, message = shop.buy_item(self.game_state, selected_item)
            self.ui.display_message(message)
            
    def _handle_selling(self, shop):
        """Handle the selling interface."""
        inventory = self.game_state.inventory
        
        if not inventory:
            self.ui.display_message("You have no items to sell.")
            return
            
        self.ui.clear_screen()
        self.ui.display_message(f"Your Items to Sell")
        self.ui.display_message(f"Your credits: {self.game_state.player.credits}")
        
        # Display all items player can sell
        options = []
        items = []
        
        for item in inventory:
            price = shop.get_sell_price(item, self.game_state.player.charm)
            options.append(f"{item.name} - {price} credits - {item.description}")
            items.append(item)
            
        options.append("Back")
        
        choice = self.ui.get_choice("Select an item to sell:", options)
        
        if choice < len(items):  # Selected an item
            selected_item = items[choice]
            success, message = shop.sell_item(self.game_state, selected_item)
            self.ui.display_message(message) 