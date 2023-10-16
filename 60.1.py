class Store:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        keys = key.split('.')
        current_dict = self.data

        for i in range(len(keys) - 1):
            if keys[i] not in current_dict:
                current_dict[keys[i]] = {}
            current_dict = current_dict[keys[i]]

        current_dict[keys[-1]] = value

    def get(self, key):
        keys = key.split('.')
        current_dict = self.data

        for k in keys:
            if k not in current_dict:
                return None
            current_dict = current_dict[k]

        return current_dict

    def delete(self, key):
        keys = key.split('.')
        current_dict = self.data

        for i in range(len(keys) - 1):
            if keys[i] not in current_dict:
                return
            current_dict = current_dict[keys[i]]

        if keys[-1] in current_dict:
            del current_dict[keys[-1]]


store = Store()

store.set('key', {'a': 1, 'b': 2, 'c': 3})

res = store.get('key')
print(res)  # {'a': 1, 'b': 2, 'c': 3}

res = store.get('key.a')
print(res)  # 1

res = store.get('key.b')
print(res)  # 2

store.delete('key.c')

res = store.get('key')
print(res)  # {'a': 1, 'b': 2}