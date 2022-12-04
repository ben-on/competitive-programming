class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pre = [nums[0]]
        post = deque([nums[-1]])
        n = len(nums)
        for i in range(1,n):
            pre.append(pre[-1]+nums[i])
            post.appendleft(post[0]+nums[-(i+1)])
        # print(pre,post)
        ans = float('inf')
        ansI = None
        for i in range(n):
            avpre = pre[i]//(i+1)
            avpost = post[i+1]//(n-i-1) if i !=n-1 else 0
            # print(avpre,avpost,avpre-avpost)
            tar = abs(avpre-avpost)
            if ans > tar:
                ans = tar
                ansI = i
        return ansI