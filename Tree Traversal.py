#AHMAD NAHID MA'ALY (1202200049)
class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

    def append(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else: #jika sudah ada charleft maka melakukan rekursi sampai ketemu yang masih kosong
                    self.left.append(data)
            elif data > self.data: #lebih besar sehingga rekursi ke kanan
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.append(data)
        else:#jika node kosong (masukan data)
            self.data = data            
    
    # Preorder traversal
    # Root -> Left ->Right
    def POTransversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.POTransversal(root.left)
         res = res + self.POTransversal(root.right)
      return res  
    # Inorder traversal
    # Left -> Root -> Right
    def IOTraversal(self, root):
        res = []
        if root:
            res = self.IOTraversal(root.left)
            res.append(root.data)
            res = res + self.IOTraversal(root.right)
        return res
    # Postorder traversal
    # Left ->Right -> Root
    def POSTTraversal(self, root):
        res = []
        if root:
            res = self.POSTTraversal(root.left)
            res = res + self.POSTTraversal(root.right)
            res.append(root.data)
        return res


while True:
    MENU = int(input("""
    --- PILIH MENU ---
    
    1. Masukan Root
    2. Masukan Child
    3. Tampilkan Tree dengan PreOrder Traversal
    4. Tampilkan Tree dengan InOrder Traversal
    5. Tampilkan Tree dengan PostOrder Traversal
    0. Selesai

    --- ()()() ---
    
    Pilih menu : """))
    if MENU == 1:
        menu = str(input('Masukan Root : '))
        root = Node(menu)
    elif MENU == 2:
        root2 = input('Masukan Target Root : ')
        root2 = root
        child = input('Membuat Child : ')
        root.append(child)
    elif MENU == 3:
        print(root.POTransversal(root))
    elif MENU == 4:
        print(root.IOTraversal(root))
    elif MENU == 5:
        print(root.POSTTraversal(root)) 
    elif MENU == 0:
        exit()