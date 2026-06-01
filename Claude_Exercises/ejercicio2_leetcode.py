class Solution(object):
    def twoSum(self, nums, target):
        
        """:type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]

lista_numeros = [2, 7, 11, 15]
encontrar_numero = 9
respuesta = Solution()
respuesta.twoSum(lista_numeros, encontrar_numero)