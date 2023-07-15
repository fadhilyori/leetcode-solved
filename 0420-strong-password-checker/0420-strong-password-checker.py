class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        missing_types = 3
        if any('a' <= c <= 'z' for c in password):
            missing_types -= 1
        if any('A' <= c <= 'Z' for c in password):
            missing_types -= 1
        if any(c.isdigit() for c in password):
            missing_types -= 1
            
        print(f"missing_types: {missing_types}")
        
        changes = 0
        one_seq = 0
        two_seq = 0
        n = len(password)
        i = 2
        
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                    
                changes += length // 3
                if length % 3 == 0:
                    one_seq += 1
                if length % 3 == 1:
                    two_seq += 1
            else:
                i += 1
        
        if n < 6:
            return max(missing_types, 6 - n)
        
        elif n <= 20:
            return max(missing_types, changes)
        
        delete_count = n - 20
        changes -= min(one_seq, delete_count)
        changes -= min(max(delete_count - one_seq, 0), two_seq * 2) // 2
        changes -= max(delete_count - one_seq - two_seq * 2, 0) // 3
        
        return delete_count + max(changes, missing_types)