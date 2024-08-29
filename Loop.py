#Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.
class Solution:
    def countNodesInLoop(self, head):
        slow = head
        fast = head
        
        # Step 1: Detect the loop using Floyd's Cycle-Finding Algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # Loop detected
            if slow == fast:
                return self.countLoopNodes(slow)
        
        # No loop detected
        return 0
    
    def countLoopNodes(self, node_in_loop):
        current = node_in_loop
        count = 1
        
        # Step 2: Count the number of nodes in the loop
        while current.next != node_in_loop:
            current = current.next
            count += 1
        
        return count
