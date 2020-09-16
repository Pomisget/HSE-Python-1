### Tasks
- [ ] [Add Binary](https://leetcode.com/problems/add-binary/)
- [ ] [Multiply strings](https://leetcode.com/problems/multiply-strings/)
- [ ] [Maximum depth of binary tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [ ] [Invert binary tree](https://leetcode.com/problems/invert-binary-tree/submissions/)
- [ ] [Same tree](https://leetcode.com/problems/same-tree/)

[:evergreen_tree: Look at this tree :evergreen_tree:](http://pythontutor.com/visualize.html#code=class%20TreeNode%3A%0A%20%20%20%20def%20__init__%28self,%20val%3D0,%20left%3DNone,%20right%3DNone%29%3A%0A%20%20%20%20%20%20%20%20self.val%20%3D%20val%0A%20%20%20%20%20%20%20%20self.left%20%3D%20left%0A%20%20%20%20%20%20%20%20self.right%20%3D%20right%0A%0A%0Anode%20%3D%20TreeNode%281%29%0Anode.left%20%3D%20TreeNode%282%29%0Anode.right%20%3D%20TreeNode%283%29%0Anode.left.left%20%3D%20TreeNode%2810%29%0A%0Aprint%28node.left.left%29%0A&cumulative=false&curInstr=26&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(10)

print(node.left.left)
```
