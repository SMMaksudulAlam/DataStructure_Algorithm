class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        ori_color = image[sr][sc]
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        row = len(image)
        col = len(image[0])
        visited = set()

        def traverse_image(sr, sc):
            visited.add((sr, sc))
            image[sr][sc] = color
            for (dr, dc) in dir:
                sr_ = sr+dr
                sc_ = sc+ dc
                if((0<=sr_<row and 0<=sc_<col) and ((sr_, sc_) not in visited) and image[sr_][sc_]==ori_color):
                    traverse_image(sr_, sc_)
            return
        traverse_image(sr, sc)
        return image