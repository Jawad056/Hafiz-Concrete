# stack.py

import json
import os

class Stack:
    def __init__(self, sizes, data_file="stock_data.json"):
        self.sizes = sizes
        self.data_file = data_file
        self.stock = self.load_stock()

    def load_stock(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                return json.load(f)
        else:
            return {size: 0 for size in self.sizes}

    def save_stock(self):
        with open(self.data_file, "w") as f:
            json.dump(self.stock, f)

    def add_slab(self, slab_size, num_slabs):
        if slab_size in self.stock:
            self.stock[slab_size] += num_slabs
            self.save_stock()
            return f"Added {num_slabs} slabs of size {slab_size}."
        else:
            return f"Size {slab_size} not available."

    def remove_slab(self, slab_size, num_slabs):
        if slab_size in self.stock:
            if self.stock[slab_size] >= num_slabs:
                self.stock[slab_size] -= num_slabs
                self.save_stock()
                return f"Removed {num_slabs} slabs of size {slab_size}."
            else:
                return f"Not enough slabs in stock to remove!"
        else:
            return f"Size {slab_size} not available."

    def get_stock(self):
        return self.stock
    
    def load_stock(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
            # If stored sizes don't match current sizes, reset stock
            if set(data.keys()) != set(self.sizes):
                return {size: 0 for size in self.sizes}
            return data
        else:
            return {size: 0 for size in self.sizes}
        
    def reset_stock(self):
        self.stock = {size: 0 for size in self.sizes}
        self.save_stock()
        return "Stock has been reset to zero."


