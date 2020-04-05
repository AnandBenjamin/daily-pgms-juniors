import java.util.*;

class Codechef
{
    Node head = null;
    
    class Node {
    int value;
    Node next;
    Node(int value) {
        this.value = value;
    }
    }
    
    public void addNode(int value) {
        Node new_node = new Node(value);
        if(this.head==null)
            this.head = new_node;
        else {
            Node current = this.head;
            while(current.next!=null){
                current=current.next;
            }
            current.next=new_node;
        }
    }
    
    public void printNodes(){
        ArrayList<Integer> al=new ArrayList<Integer>();
        Node current=this.head;
        while(current!=null) {
            al.add(current.value);
            current=current.next;
        }
        System.out.println(al);
    }
    
    public int removeHead() {
        if(this.head==null)
            return -1;
        else {
            Node current = this.head;
            head = current.next;
            return current.value;
        }
    }
    
    public int removeTail() {
        if(this.head==null)
            return -1;
        else {
            Node current = this.head;
            Node prev = null;
            while(current.next!=null){
                prev=current;
                current=current.next;
            }
            
            if(prev!=null)
                prev.next=null;
            else
                this.head=null;
                
            return current.value;
        }
    }
    
    public void addHead(int value) {
        Node new_node = new Node(value);
        Node current = this.head;
        
        if(current!=null)
            new_node.next=current;
            
        this.head=new_node;
    }
    
    public void insertAtPosition(int pos, int value) {
        Node new_node = new Node(value);
        Node current = this.head;
        Node prev = null;
        int index = 1;
        
        while(index<pos&&current!=null) {
        	prev = current;
        	current = current.next;
        	index++;
        }
        
        if(pos==1) {
        	this.head = new_node;
        	new_node.next=current;
        	return;
        }
        
        if(pos==index && prev!=null) {
        	prev.next = new_node;
            new_node.next = current;
        } else {
        	System.out.println("Index: " + pos + " not found in the List to insert element");
        }
            
    }

    public int deleteAtPosition(int pos) {
        Node current = this.head;
        Node prev = null;
        int index = 1;
        
        while(index<pos&&current!=null) {
        	prev = current;
        	current = current.next;
        	index++;
        }
        if(pos==1) {
        	this.head = current.next;
        	return current.value;
        }
    	if(pos==index && current!=null) {
	    	prev.next = current.next;
	    	return current.value;
        } else 
        	return -1;
    }

    public void deleteValue(int value) {
    	Node current = this.head;
    	Node prev = null;
    			
    	while(current!=null && current.value!=value) {
    		prev = current;
    		current = current.next;
    	}
    	
    	if(current==null)
    		System.out.println("Value: " + value + " not found in list");
    	else {
    		if(prev==null)
    			this.head = current.next;
    		else
    			prev.next = current.next;
    	}
    }
    
    public static void main (String[] args) throws java.lang.Exception
	{
		Codechef obj = new Codechef();
		
		obj.addNode(5);
		obj.addNode(10);
		obj.printNodes();
		
		System.out.println("Removing head from above list:" + obj.removeHead());
		obj.printNodes();
		
		obj.addNode(15);
		obj.printNodes();
		
		System.out.println("Removing Tail from above list:" + obj.removeTail());
		obj.printNodes();
		
		System.out.println("Removing Tail from above list:" + obj.removeTail());
		obj.printNodes();
		
		System.out.println("Removing Tail from above list:" + obj.removeTail());
		
 		obj.addHead(20);
 		obj.printNodes();
		
 		obj.addHead(25);
 		obj.printNodes();
		
 		obj.insertAtPosition(3, 33);
		obj.insertAtPosition(1, 11);
		obj.insertAtPosition(2, 22);
		obj.insertAtPosition(7, 77);
		obj.printNodes();
		
		System.out.println("Deleting at position 1: " + obj.deleteAtPosition(1));
		obj.printNodes();
		System.out.println("Deleting at position 3: " + obj.deleteAtPosition(3));
		obj.printNodes();
		System.out.println("Deleting at position 5: " + obj.deleteAtPosition(5));
		obj.printNodes();
		System.out.println("Deleting at position 7: " + obj.deleteAtPosition(7));
		obj.printNodes();
		
		obj.deleteValue(20);
		obj.printNodes();
		obj.deleteValue(33);
		obj.printNodes();
		obj.deleteValue(77);
		obj.printNodes();
		obj.deleteValue(22);
		obj.printNodes();
		
	}
}
