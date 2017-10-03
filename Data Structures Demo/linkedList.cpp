// Steven DeMartini
//11/1/16
//ch 17 assignment 5
//linked lists
#include <iostream>
#include <string>
class LinkedList
{
protected:
    struct Node
    {
        int value;
        Node *next;
        Node(int val1, Node *next1 = NULL)
        {
            value = val1;
            next = next1;
        }
    };
    Node *head;
public:
    LinkedList() {head = NULL;}
    ~LinkedList();
    void append(int number);
    void remove(int number);
    void insert(int number);
    void printList();
};

void LinkedList::insert(int number)
{
    Node *nodePtr, *previousNodePtr;
    
    if (head == NULL || head->value >= number)
    {
        // A new node goes at the beginning of the list.
        head = new Node(number, head);
    }
    else
    {
        previousNodePtr = head;
        nodePtr = head->next;
        
        // Find the insertion point.
        while (nodePtr != NULL && nodePtr->value < number)
        {
            previousNodePtr = nodePtr;
            nodePtr = nodePtr->next;
            
        }
        // Insert the new node just before nodePtr.
        previousNodePtr->next = new Node(number, nodePtr);
    }
}

//remove
void LinkedList::remove(int number)
{
    Node *nodePtr, *previousNodePtr;
    
    // If the list is empty, do nothing.
    if (!head) return;
    // Determine if the first node is the one to delete.
    if (head->value == number)
    {
        nodePtr = head;
        head = head->next;
        delete nodePtr;
    }
    else
    {
        // Initialize nodePtr to the head of the list.
        nodePtr = head;
        
        // Skip nodes whose value member is not number
        while (nodePtr != NULL && nodePtr->value != number)
        {
            previousNodePtr = nodePtr;
            nodePtr = nodePtr->next;
        }
        // Link the previous node to the node after
        // nodePtr, then delete nodePtr.
        if (nodePtr)
        {
            previousNodePtr->next = nodePtr->next;
            delete nodePtr;
        }
    }
}

//add
void LinkedList::append(int number)
{
    if (head == NULL)
        head = new Node(number);
    else
    {
        // The list is not empty.
        // Use nodePtr to traverse the list
        Node *nodePtr = head;
        while (nodePtr->next != NULL)
            nodePtr = nodePtr->next;
        
        nodePtr->next = new Node(number);
    }
}

//destructor
LinkedList::~LinkedList()
{
    Node *nodePtr = head; // Start at head of list
    while (nodePtr != NULL)
    {
        // garbage keeps track of node to be deleted
        Node *garbage = nodePtr;
        // Move on to the next node, if any
        nodePtr = nodePtr->next;
        // Delete the "garbage" node
        delete garbage;
    }
}

//print
void LinkedList::printList()
{
    Node *nodePtr = head; // Start at head of list
    while (nodePtr)
    {
        // Print the value in the current node
        std::cout << nodePtr->value << " ";
        // Move on to the next node
        nodePtr = nodePtr->next;
    }
    std::cout << "\n";
}


int main()
{
    LinkedList list;
    list.append(2);
    list.append(7);
    list.append(12);
    list.append(5);
    list.printList();
    std::cout << "going to remove 5 \nnew list \n";
    list.remove(5);
    list.printList();
    std::cout << "going to insert 6 and 8 \nnew list \n";
    list.insert(6);
    list.insert(8);
    list.printList();
    
    
    std::string name;
    getline (std::cin, name);
    std::cout << "Hello, " << name << "!\n";
}
