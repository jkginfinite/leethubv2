# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def reserialize(root, string):
            if root is None:
                string+='None,'
            else:
                string+=str(root.val)+','
                string=reserialize(root.left,string)
                string=reserialize(root.right,string)
            return string
        return reserialize(root,'')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode"""
        def rdeserialize(l):
            if l[0]=='None':
                l.pop(0)
                return None
            
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root
        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root
