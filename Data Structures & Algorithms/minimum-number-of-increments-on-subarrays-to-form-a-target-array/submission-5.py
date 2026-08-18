class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        complete_when = max(target)
        operation_count = 0
        counter = 1

        while counter <= complete_when:
            idx = 0
            operation_is_running = False

            while idx < len(target):
                # Traverse a complete list
                val = target[idx]

                if val < counter:
                    # Track a disjunct in subarrays
                    operation_is_running = False

                else:
                    # Mod needed 
                    if not operation_is_running:
                        # Track beginning of new subarray
                        operation_count += 1
                        operation_is_running = True
                
                idx += 1
            counter += 1
            
        return operation_count
        