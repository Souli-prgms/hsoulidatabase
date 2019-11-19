class Database:
    def __init__(self, core_node):
        self.nodes = {core_node: None}
        self.core = core_node
        self.tree = {core_node: []}
        self.block = False
        self.extracts = {}
        self.status = {core_node: 0}
        self.status_type = {0: "valid", 1: "granularity_staged", 2: "coverage_staged", 3: "invalid"}

    def add_nodes(self, nodes):
        for node, parent in nodes:
            self.nodes[node] = parent

            if self.block:
                self.update_status(parent, node)

            else:
                self.tree[parent].append(node)
                self.tree[node] = []
                self.status[node] = 0  # valid label

    def add_extract(self, new_extract):
        for extract, labels in new_extract.items():
            self.extracts[extract] = labels
        self.block = True

    def get_extract_status(self):
        status = {}

        for extract, labels in self.extracts.items():
            if len(labels) > 0:
                extract_statuses = [self.status[label] if label in self.nodes else 3 for label in
                                    labels]  # 3 stands for invalid label

                status[extract] = self.status_type[max(extract_statuses)]

            else:
                status[extract] = self.status_type[0] # valid

        return status

    def update_status(self, parent, node):
        # Child nodes
        for child in self.tree[parent]:
            self.update_node_status(child, 2)  # coverage_staged

        # Parent
        self.update_node_status(parent, 1)  # granularity_staged

    def update_node_status(self, node, value):
        if node != self.core:
            self.status[node] = max(value, self.status[node])