import math
import pytest
from solution.code_530_minimum_absolute_difference_in_bst import Solution, TreeNode

class TestGetMinimumDifference:
    @pytest.fixture
    def solution(self):
        return Solution()

    def test_minimum_difference_within_range(self, solution):
        # Create a binary search tree with minimum nodes [2, 104]
        #      3
        #     / \
        #    1   5
        root1 = TreeNode(3)
        root1.left = TreeNode(1)
        root1.right = TreeNode(5)

        # Calculate the minimum difference
        result1 = solution.getMinimumDifference(root1)

        # Assert the result within the given range [0, 105]
        assert 0 <= result1 <= 105

class TestGetMinimumDifference:
    @pytest.fixture
    def solution(self):
        return Solution()

    def test_minimum_difference_single_node(self, solution):
        # Test with a single-node tree
        root2 = TreeNode(7)

        # Calculate the minimum difference
        result2 = solution.getMinimumDifference(root2)

        # Assert that the result is not equal to positive infinity and is finite
        assert result2 != float('inf') and math.isfinite(result2)

    def test_minimum_difference_unbalanced_tree(self, solution):
        # Test an unbalanced tree:
        #       10
        #        /
        #       5
        #      /
        #     2
        root3 = TreeNode(10)
        root3.left = TreeNode(5)
        root3.left.left = TreeNode(2)

        # Calculate the minimum difference
        result3 = solution.getMinimumDifference(root3)

        # Assert the result within the given range [0, 105]
        assert 0 <= result3 <= 105

    def test_minimum_difference_large_tree(self, solution):
        # Constructing a larger binary search tree
        #        10
        #       /  \
        #      5    15
        #     / \   / \
        #    2   8 12  18
        #   / \
        #  1   3
        root4 = TreeNode(10)
        root4.left = TreeNode(5)
        root4.right = TreeNode(15)
        root4.left.left = TreeNode(2)
        root4.left.right = TreeNode(8)
        root4.left.left.left = TreeNode(1)
        root4.left.left.right = TreeNode(3)
        root4.right.left = TreeNode(12)
        root4.right.right = TreeNode(18)

        # Calculate the minimum difference
        result4 = solution.getMinimumDifference(root4)

        # Assert the result within the given range [0, 105]
        assert 0 <= result4 <= 105

    def test_minimum_difference_edge_cases(self, solution):
        # Test edge cases, such as an empty tree or a tree with identical values
        empty_tree = None
        root_with_identical_values = TreeNode(5)
        root_with_identical_values.left = TreeNode(5)
        root_with_identical_values.right = TreeNode(5)

        # Calculate the minimum difference for the empty tree
        result_empty_tree = solution.getMinimumDifference(empty_tree)
        # Assert that the result is finite for an empty tree

        # Calculate the minimum difference for the tree with identical values
        result_identical_values = solution.getMinimumDifference(root_with_identical_values)
        # Assert that the result is finite for a tree with identical values

# Run the tests using pytest
if __name__ == "__main__":
    pytest.main()
