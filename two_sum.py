class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_freqs = self.freq_counter(nums)

        idxs = []

        for num_idx in range(len(nums)):
            # print("idx", num_idx)
            val = target - nums[num_idx]

            # print("val", val)
            # print("num_freqs", num_freqs)

            if val in num_freqs:
                if val == nums[num_idx]:
                    if not num_freqs[val] >= 2:
                        continue
                idxs.append(num_idx)
                idxs.append(self.find_num(val, nums))
                break

        return idxs


    def freq_counter(self, iter):
        freqs = {}

        for i in iter:
            if i in freqs:
                freqs[i] += 1
            else:
                freqs[i] = 1

        return freqs

    def find_num(self, num, nums):
        i = len(nums) - 1

        while i >= 0:
            if nums[i] == num:
                return i
            i -= 1

# test = Solution()

# two_sum = test.twoSum([3,2,4], 6)

# print(two_sum)

