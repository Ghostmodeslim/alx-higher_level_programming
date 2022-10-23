#!/usr/bin/python3
"""A pascal_triangle module"""


def pascal_triangle(n):
        if n <= 0:
                return([''])

        pascal = [[1]]
        for cur_row in range(1, n):
                row = [1]
                prev_row = pascal[cur_row - 1]
                for num in range(1, cur_row):
                        row.append(prev_row[num] + prev_row[num - 1])
                row.append(1)
                pascal.append(row)
        return(pascal)
