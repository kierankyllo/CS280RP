## Evaluating Age and Gender Inference Bias: Microsoft Azure Cognitive Services

### Abstract

Computer vision is a rapidly growing and increasingly mainstream usage of modern machine learning techniques.  Inference on images of the human facial form is becoming increasingly common in applications such as law enforcement, intelligence gathering, marketing, sentiment analysis, lip reading, and biometrics.  This study investigates inference bias present in the Microsoft Azure Cognitive Services Face API by exposing a sample of 67,228 facial raster images from the manually annotated Fairface dataset.  Detection rates, gender inference error rates, and age inference error rates are compared across seven racial categories by chi square test at p < 0.001.  Black faces were over represented in detection failure and gender inference error rates while white faces were most associated with age inference failure rates with a positive correlation to age overestimation. Azure Cognitive Services was most accurate when inferring the gender of White subjects and when inferring the age of East Asian facial images with inference errors positively correlated with age underestimation. These findings highlight and replicate the mounting evidence of computer vision biases present in the literature generally and may point to specific bias mechanics not yet well understood.  


### Hypotheses:  

•	HO : The error rate will be equal across all race categories with respect to gender and age inference values at  p < 0.001 (No evidence of difference).

•	HA : Statistically significant differences in error rates exist between race categories with respect to gender and age at  p < 0.001. (Evidence of difference exists).


**References:**

Buolamwini, J., & Gebru, T. (2018). Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification. Proceedings of Machine Learning Research, 81, 77–91. https://doi.org/http://proceedings.mlr.press/v81/buolamwini18a.html 

Farley, P. (n.d.). Call the detect API - face - azure cognitive services. Face - Azure Cognitive Services | Microsoft Docs. Retrieved October 26, 2021, from https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/howtodetectfacesinimage. 

Karkkainen, K., & Joo, J. (2021). Fairface: Face attribute dataset for balanced race, gender, and age for bias measurement and mitigation. 2021 IEEE Winter Conference on Applications of Computer Vision (WACV). https://doi.org/10.1109/wacv48630.2021.00159 

The chi squared tests: The BMJ. The BMJ | The BMJ: leading general medical journal. Research. Education. Comment. (2021, April 12). Retrieved October 26, 2021, from https://www.bmj.com/about-bmj/resources-readers/publications/statistics-square-one/8-chi-squared-tests.

