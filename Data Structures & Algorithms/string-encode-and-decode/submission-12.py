class Solution:
    delimiter = "#"

    def encode(self, strs: List[str]) -> str:
        out = ""
        for string in strs:
            out += f'{len(string)}{self.delimiter}{string}'
        return out

    def decode(self, s: str) -> List[str]:
        out, i = [], 0

        while i < len(s):
            char = s[i]
            # We can assume we begin w / delimiter; 
            # Need to determine its length
            num_digits = 0
            j = i
            next_str_len = ""
            while j < len(s) and s[j].isdigit():
                num_digits += 1
                next_str_len += s[j]
                j += 1

            # Slice & append string: starting after deliminter to end of len
            starting_i = i + num_digits + len(self.delimiter)
            ending_i = starting_i + int(next_str_len)
            out.append(s[starting_i : ending_i])
            # Jump past delimiters to the next encoded char
            i = ending_i

        return out


    # How do we know that "#" itself is not in the string? And number treatment? 
    # A - we don't. We do know that 
    # Critique of own code here: 
    # -- you'll now never need this else loop because you're always jumping to the next str
    #  -- some aspects feel more readable but it is pretty verbose and not all vars are needed

    # class Solution:
    # delimiter = "#"

    # def encode(self, strs: List[str]) -> str:
    #     out = ""
    #     for string in strs:
    #         out += f'{len(string)}{self.delimiter}{string}'
    #     return out

    # def decode(self, s: str) -> List[str]:
    #     out = []
    #     i = 0

    #     while i < len(s):
    #         char = s[i]

    #         # Is this the delimiter marker?
    #         this_is_new_str = False
    #         if char.isdigit():
    #             # Determine num digits for str len marker
    #             num_digits = 0
    #             j = i
    #             next_str_len = ""
    #             while j < len(s) and s[j].isdigit():
    #                 num_digits += 1
    #                 next_str_len += s[j]
    #                 j += 1

    #             # Test for delimiter end
    #             if i + num_digits < len(s) and s[i + num_digits] == self.delimiter:
    #                 this_is_new_str = True

    #         if this_is_new_str:
    #             # Slice & append string: starting after deliminter to end of len
    #             starting_i = i + num_digits + len(self.delimiter)
    #             ending_i = starting_i + int(next_str_len)
    #             out.append(s[starting_i : ending_i])
    #             # Jump past delimiters to the next encoded char
    #             i = ending_i
    #         else:
    #             out[-1] += char
    #             i += 1
    #     return out