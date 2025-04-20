from typing import Optional

class ArvoreNodulo :
    def __init__(self, val=0, left=None, right=None):
        self.val
        self.left
        self.right
        
class Solucao:
    def inverterArvore(self, root: Optional[ArvoreNodulo]) -> Optional[ArvoreNodulo]:
        
        def invercionar(root):
            if root:
                root.left, root.right = root.right, root.left
                invercionar(root.left), invercionar(root.right)
                
        invercionar(root)
        return root

