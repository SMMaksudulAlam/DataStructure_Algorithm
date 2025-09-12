class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        e_s = "π".join(strs)
        return e_s

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        lst = s.split("π")
        return lst
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))