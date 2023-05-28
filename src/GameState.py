import pandas

class ProcessGameState:
    weapons = dict()
    total_ticks = 0
    ticks_in_region = 0

    def _parseWeapons(self, inventory):
        if inventory is None:
            return

        for weapon_dict in inventory:
            key_list = self.weapons.get(weapon_dict.get("weapon_class"))

            if key_list is None:
                key_list = []

            weapon_name = weapon_dict.get("weapon_name")
            if weapon_name not in key_list:
                key_list.append(weapon_name)
                self.weapons[weapon_dict.get("weapon_class")] =  key_list

    def _parseInBoundary(self, x, y, z):
        z_max, z_min = 421, 285
        boundary = [
            [-1735, 250], [-2024, 398], [-2806, 742], 
            [-2472, 1233], [-1565, 580]
        ]

    def _parseData(self):
        for row in self.data_frame:
            side = row["side"]
            if side == "T":
                x, y, z = row["x"], row["y"], row["z"]
                self._parseInBoundary(x, y, z)


    def __init__(self, file):
        self.data_frame = pandas.read_parquet(file)
        self._parseData()
        print(self.weapons)