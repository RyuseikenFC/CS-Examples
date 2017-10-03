// Steven DeMartini
// cs 3
// binary tree
// ch 20
#include <string>
#include <iostream>

template <class T>
class Tree
{
    // Internal class which stores only Node related information.
    struct TreeNode
    {
        T data;
        TreeNode * left;
        TreeNode * right;
        
        TreeNode(T val):data(val),left(NULL),right(NULL)
        {
        }
    };
    TreeNode * root;
    void print(TreeNode*);
    void freeMemory(TreeNode*);
    void Delete(T, TreeNode*);
    bool search(T, TreeNode*);
    void makeDeletion(TreeNode*);
    void remove();
    
    
public:
    Tree();
    ~Tree();
    void insert(T);
    void print();
    bool search(T);
    void Delete(T);
};

template <class T>
Tree<T>::Tree():root(NULL){}

template <class T>
Tree<T>::~Tree()
{
    freeMemory(root);
}

template <class T>
void Tree<T>::freeMemory(Tree::TreeNode *node)
{
    if (node==NULL)
        return;
    if (node->left)
        freeMemory(node->left);
    if (root->right)
        freeMemory(node->right);
    delete node;
}

template <class T>
//make it return value?
void Tree<T>::insert(T val)
{
    TreeNode * treeNode = NULL;
    try
    {
        treeNode = new TreeNode(val); // handle exception necessary?
    } catch (std::bad_alloc &exception)
    {
        std::cerr << "bad_alloc caught: " << exception.what() << std::endl;
        EXIT_FAILURE;
    }
    TreeNode *temp=NULL;
    TreeNode *prev=NULL;
    
    temp = root;
    while(temp)
    {
        prev = temp;
        if (temp->data < treeNode->data)
            temp = temp->right;
        else
            temp = temp->left;
    }
    if (prev==NULL)
        root = treeNode;
    else
    {
        if (prev->data<treeNode->data)
            prev->right = treeNode;  // use setter function?
        else
            prev->left = treeNode;
    }
}

template <class T>
void Tree<T>::print(TreeNode *root)
{
    if (root==NULL)
        return ;
    print(root->left);
    std::cout << root->data << " ";
    print(root->right);
}

template <class T>
void Tree<T>::print()
{
    print(root);
}

//search
template <class T>
bool Tree<T>::search(T val, Tree::TreeNode *leaf)
{
    if(leaf!=NULL)
    {
        if(val==leaf->data)
            return true;
        if(val<leaf->data)
            return search(val, leaf->left);
        else
            return search(val, leaf->right);
    }
    else return false;
}

template <class T>
bool Tree<T>::search(T val)
{
    return search(val, root);
}

template <class T>
void Tree<T>::Delete(T val)
{
    Delete(val, root);
}

template <class T>
void Tree<T>::makeDeletion(Tree::TreeNode *tree)
{

    TreeNode *nodeToDelete = tree;
    TreeNode *attachPoint;
    if (tree->right == NULL)
    {
        tree = tree->left;
    }
    else if (tree->left == NULL)
    {
        tree = tree->right;
    }
    else
    {
        attachPoint = tree->right;
        while (attachPoint->left != NULL)
            attachPoint = attachPoint->left;
        attachPoint->left = tree->left;
        tree = tree->right;
    }
    delete nodeToDelete;
}


//delete
template <class T>
void Tree<T>::Delete(T val, Tree::TreeNode *tree)
{
    if (tree == NULL) return;
    if (val< tree->data)
        Delete(val, tree->left);
    else if (val > tree->data)
        Delete(val, tree->right);
    else
        // We have found the node to delete.
        makeDeletion(tree);
}

int main()
{
    Tree<int> tree;
    tree.insert(14);
    tree.insert(12);
    tree.insert(6);
    tree.insert(17);
    tree.insert(8);
    tree.print();
    std::cout <<"\n";
    
    std::cout << "is 8 in the tree? "<<"\n";
    if(tree.search(8) == true)
        std::cout << "8 is in the tree" <<"\n";
    
    tree.Delete(8);
    tree.print();
}
