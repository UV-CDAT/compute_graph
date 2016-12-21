import unittest
import compute_graph


class TestComputeNode(unittest.TestCase):
    def test_attribute_management(self):
        node = compute_graph.ComputeNode(key="hi", other_key=2)
        self.assertTrue(hasattr(node, "key"))
        self.assertTrue(hasattr(node, "other_key"))
        self.assertEqual(node.key, "hi")
        self.assertEqual(node.other_key, 2)
        node.test_setattr = "test"
        self.assertTrue(hasattr(node, "test_setattr"))
        self.assertEqual(node.test_setattr, "test")

    def test_dependencies(self):
        node = compute_graph.ComputeNode(key="hi", other_key=2)
        child_node = compute_graph.ComputeNode(value=node)
        other_child = compute_graph.ComputeNode(value=node)
        last_descendant = compute_graph.ComputeNode(parent=child_node, parent2=other_child)

        deps = last_descendant.dependencies()
        self.assertEqual(deps[0], node)
        if deps[1] not in (child_node, other_child):
            self.assertTrue(False, "Incorrect dependency order")
        if deps[2] not in (child_node, other_child):
            self.assertTrue(False, "Incorrect dependency order")
        self.assertEqual(deps[3], last_descendant)
