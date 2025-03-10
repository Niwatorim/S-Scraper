from singlepage import scrape, splitter
from AI_response import sort
import asyncio
import sys



async def webscraper(prompt):
    print('Prompt is: ',prompt)
    content = await scrape()
    print('Hadith scraped')
    chunks = splitter(content)
    print('hadith split')
    response = await sort(prompt,chunks)
    print(response)
    return response

asyncio.run(webscraper('I want Hadith about intentions'))


#Result: when prompt is 'Hadith about intention'
'''
Page scraped
Hadith scraped
Hadith obtained
hadith split
Parsed batch 1 of 3
Parsed batch 2 of 3
Parsed batch 3 of 3
| **Relevance Score** | **Hadith Text** |
| --- | --- |
| 9/10 | Narrated 'Umar bin Al-Khattab: I heard Allah's Messenger (ﷺ) saying, "The reward of deeds depends upon the intentions and every person will get the reward according to what he has intended. So whoever emigrated for worldly benefits or for a woman to marry, his emigration was for what he emigrated for." |
| 8/10 | Narrated 'Aisha: (the mother of the faithful believers) Al-Harith bin Hisham asked Allah's Messenger (ﷺ) "O Allah's Messenger (ﷺ)! How is the Divine Inspiration revealed to you?" Allah's Messenger (ﷺ) replied, "Sometimes it is (revealed) like the ringing of a bell... " |
| 7/10 | Narrated 'Aisha: The commencement of the Divine Inspiration to Allah's Messenger (ﷺ) was in the form of good dreams which came true like bright daylight, and then the love of seclusion was bestowed upon him. He used to go in seclusion in the cave of Hira where he used to worship (Allah alone) continuously for many days before his desire to see his family... |
| 6/10 | Narrated Jabir bin 'Abdullah Al-Ansari: While I was walking, all of a sudden I heard a voice from the sky. I looked up and saw the same angel who had visited me at the cave of Hira' sitting on a chair between the sky and the earth... |
| 5/10 | Narrated Said bin Jubair: Ibn 'Abbas in the explanation of the statement of Allah "Move not your tongue concerning (the Quran) to make haste therewith." said "Allah's Messenger (ﷺ) used to bear the revelation with great trouble and used to move his lips (quickly) with the Inspiration." |
**Hadith Analysis Results**

| Relevance Score | Hadith Text |
| --- | --- |
| 8/10 | Narrated Ibn 'Abbas: Allah's Messenger (ﷺ) was the most generous of all the people, and he used to reach the peak in generosity in the month of Ramadan when Gabriel met him. [1] |

**Explanation**

The hadith narrated by Ibn Abbas highlights the Prophet Muhammad's (peace be upon him) generosity, particularly during the month of Ramadan. The mention of intentions is implicit in the context, as the Prophet's actions are driven by his commitment to charitable deeds and devotion to Allah.

**Relevance Score Breakdown:**

* **Content match**: 5/5 (the hadith mentions the Prophet's generosity and charitable actions)
* **Contextual relevance**: 2/5 (while intentions are not explicitly stated, they can be inferred from the context of charity and devotion)

Note that a lower score is given for contextual relevance as the concept of "intentions" could be interpreted in various ways. However, this hadith does demonstrate the Prophet's actions being guided by his devotion to Allah and commitment to charitable deeds.
| Relevance Score | Hadith Text |
| --- | --- |
| 80% | “The Messenger of Allah (peace be upon him) said, ‘There will be no harm on a non-believer who has not been given the revelation or who has not come to know that what he has been worshipping is not the truth.’” [Musnad Ahmad (2/344), Al-Khatib al-Baghdadi's Ta'rikh Baghdad (3/349)] |
| 70% | “I heard Allah’s Messenger (peace be upon him) say, ‘The person who was a hypocrite at the time of the Prophet will not taste death until he sees that which he hates most.’” [Sahih Muslim (53:56), Sahih Bukhari (73:1)] |
| 60% | “Abu Hurairah reported Allah’s Messenger (peace be upon him) as saying, ‘When a hypocrite is in the company of people, he will not die until he sees what he hates most.’” [Sahih Muslim (53:57), Sahih Bukhari (73:1)] |
| 50% | “The Prophet (peace be upon him) said, ‘A person who was given revelation and did not follow it will have no share in the hereafter.” [Musnad Ahmad (4/258), Sunan Tirmidhi (47:13)] |
| 40% | “Abu Hurairah reported Allah’s Messenger (peace be upon him) as saying, ‘There will come a time when people will not obey the leaders and there will be such disorder that the one who is most capable of ruling will wish to be in the mountains or deserts.’” [Sahih Muslim (50:56), Sahih Bukhari (73:1)] |

Note:

* The Relevance Score is subjective and based on my analysis of the text.
* Some parts of the hadiths may not directly relate to the original article, but they convey related ideas or principles.
* The scores are out of 100 and reflect how closely the hadith texts align with the themes presented in the original article.

Please keep in mind that this is an automated analysis, and while I strive for accuracy, there might be some room for interpretation. If you'd like me to re-evaluate the results or provide more information on a specific hadith, feel free to ask!
'''