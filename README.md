## Evaluating Age and Gender Inference Bias: Microsoft Azure Cognitive Services

Computer vision is a rapidly growing and increasingly mainstream usage of modern machine learning techniques.  When applied to the human image, computer vision and machine learning inference tools are capable of increasingly accurate and potentially useful categorical inference from raster data.  However, efforts to evaluate commercially available algorithm APIs have shown bias in gender discernment in sample sets representing POC populations. (Buolamwini & Gebru, 2018) I propose a similar examination of the commercially available MS Azure Cognitive Services Face API in an effort to quantify bias inherent in the service when applied to annotated facial images.

The intent of this research effort is to measure and compare error rates in facial inference for gender and age across ethnically diverse population samples.  This research will reveal if statistically significant differences exists in the error rates of inferences made by the MS Azure Face API with respect to gender and age across racially diverse sample groups. For example, does the API infer a younger age for white faces? Is gender inference less accurate for darker skinned ethnic groups? Is the API more accurate for the faces of men from lighter skinned ethnic groups? etc.

To accomplish this goal, the ‘Fairface’ dataset will be used as the annotated ground truth of gender, age, and ethnic group membership.  (Karkkainen & Joo, 2021) The Microsoft Azure cognitive services API will be called with an image from the dataset and will return inference values for age and gender.  This will be accomplished using python scripting and the Azure Cognitive Services Face API libraries. The proportion of the error rate of returned values will be assessed by chi-squared test across the ethnic groups and with respect to overall accuracy. (The BMJ, 2021) 

**-The NULL hypothesis is that the error rate will be equal across all ethnic groups with respect to gender and age inference values at P > 0.001 (no evidence of difference).**

**-The alternative hypothesis is that statistically significant differences in error rates exist between ethnic groups with respect to gender and age. (evidence of difference exists).**

**References:**

Buolamwini, J., & Gebru, T. (2018). Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification. Proceedings of Machine Learning Research, 81, 77–91. https://doi.org/http://proceedings.mlr.press/v81/buolamwini18a.html

PatrickFarley. (n.d.). Call the detect API - face - azure cognitive services. Face - Azure Cognitive Services | Microsoft Docs. Retrieved October 26, 2021, from https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/howtodetectfacesinimage. 

Karkkainen, K., & Joo, J. (2021). Fairface: Face attribute dataset for balanced race, gender, and age for bias measurement and mitigation. 2021 IEEE Winter Conference on Applications of Computer Vision (WACV). https://doi.org/10.1109/wacv48630.2021.00159 

The chi squared tests: The BMJ. The BMJ | The BMJ: leading general medical journal. Research. Education. Comment. (2021, April 12). Retrieved October 26, 2021, from https://www.bmj.com/about-bmj/resources-readers/publications/statistics-square-one/8-chi-squared-tests. 
