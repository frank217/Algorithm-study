'''
https://leetcode.com/problems/minimum-number-of-people-to-teach/
'''


from collections import defaultdict
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Define Language as set
        ldic = defaultdict(set)
        for userId in range(len(languages)):
            for l in languages[userId]:
                ldic[l].add(userId+1)
        print(ldic)

        friendshipWithRemoved = []
        for friendship in friendships: 
            u1,u2 = friendship
            shareLanguage = False
            for language in ldic:
                languageGroup = ldic[language]
                if u1 in languageGroup and u2 in languageGroup: 
                    shareLanguage = True
            if not shareLanguage:
                friendshipWithRemoved.append(friendship)


        #Loop through each language an see how many we need to teach
        minNumbertoTeach = len(languages)
        for language in range(1,n+1):
            userThatNeedTeaching = set()
            usersThatKnowThisLanguage = ldic[language]
            for friendship in friendshipWithRemoved: 
                u1,u2 = friendship
                if u1 not in usersThatKnowThisLanguage:
                    userThatNeedTeaching.add(u1)
                if u2 not in usersThatKnowThisLanguage:
                    userThatNeedTeaching.add(u2)
            #print(language,len(userThatNeedTeaching))
            minNumbertoTeach = min(minNumbertoTeach,len(userThatNeedTeaching))
        
        return minNumbertoTeach