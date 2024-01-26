# Your TreeNode and Solution classes go here...

import pytest
from solution.code_637_average_of_levels_in_binary_tree import TreeNode, Solution

@pytest.fixture
def example_binary_tree():
    # Example binary tree:
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

def test_averageOfLevels(example_binary_tree):
    # The averages at each level are: [3, (9 + 20) / 2, (15 + 7) / 2] = [3, 14.5, 11]
    solution = Solution()
    result = solution.averageOfLevels(example_binary_tree)
    assert result == [3.0, 14.5, 11.0]

def test_emptyTree():
    # Test an empty tree
    root = None
    solution = Solution()
    result = solution.averageOfLevels(root)
    assert result == []

def test_singleNodeTree():
    # Test a tree with only one node
    root = TreeNode(5)
    solution = Solution()
    result = solution.averageOfLevels(root)
    assert result == [5.0]

def test_unbalancedTree():
    # Test an unbalanced tree:
    #       1
    #        \
    #         2
    #          \
    #           3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)

    solution = Solution()
    result = solution.averageOfLevels(root)

    # The averages at each level are: [1, 2, 3] = [1, 2, 3]
    assert result == [1.0, 2.0, 3.0]

def test_negativeValues():
    # Test a tree with negative values:
    #       -5
    #      / \
    #    -10  -3
    #    /    / \
    #   6   -8   1
    root = TreeNode(-5)
    root.left = TreeNode(-10)
    root.left.left = TreeNode(6)
    root.right = TreeNode(-3)
    root.right.left = TreeNode(-8)
    root.right.right = TreeNode(1)

    solution = Solution()
    result = solution.averageOfLevels(root)

    # Use a larger tolerance for floating-point comparison
    assert all(abs(a - b) < 1e-3 for a, b in zip(result, [-5.0, -6.5, -0.333]))

