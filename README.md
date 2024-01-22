# **PBL6 - Detect AI Generated Face**

## **Introduction**

With the rapid development of Artificial Intelligence (AI), followed by the emergence of AI-generated images, distinguishing between images created by AI and real images has become increasingly challenging. Technological advancements have raised concerns about reliability and safety in various domains such as information security, privacy, copyrights, etc. This is particularly crucial for identity-related data, such as human facial images. Currently, despite numerous studies focusing on building deep learning models to differentiate between real and AI-generated images, these models have not yet achieved consistently high accuracy with data from newer image generation models. There is also a limited focus on human facial data, and existing research has not been widely applied in real-world systems. In this study, we undertook the construction of a dataset consisting of human facial images generated by the latest AI image generation models. We propose several deep learning models based on Convolutional Neural Network architectures and Transfer Learning - Ensemble Learning techniques to detect AI-generated human facial images and real human facial images. Additionally, we develop a website system to integrate research results, allowing users easy interaction and utilization. Through testing and evaluation on the constructed dataset, the results demonstrate the effectiveness of the models, with the highest accuracy reaching up to 97.91%. The system also exhibits fast processing speeds, averaging 7-8 seconds per image for the classification process and around 70 - 74 seconds per image for result explanation.

## **Repository Structure**

- **`/Data`**: contains the processing code to collect, augment, and split the dataset.
- **`/Notebooks`**: contains the code to train and evaluate the models.
- **`/Frontend`**: contains the frontend code of the website.
- **`/Server`**: contains the backend code of the website based on FastAPI.
- **`/Report`**: contains the report of the project.

## **Dataset**

In summary, our team has built a dataset comprising 120,959 images belonging to two classes: real images (70,000 images) and AI-generated images (50,959 images). You can download the dataset [here](https://www.kaggle.com/datasets/philosopher0808/real-vs-ai-generated-faces-dataset).

| Class               | Data source                | Số lượng ảnh |
|---------------------|----------------------------|--------------|
| Real faces          | FFHQ                       | 70,000       |
| AI Generated        | thispersondoesnotexist.com | 20,499       |
|                     | SFHQ                       | 20,000       |
|                     | Swap face                  | 9,429        |
|                     | Stable Diffusion           | 1,031        |

## **Contributors**

- Cao Kieu Van Manh
- Nguyen Tuan Hung
- Vo Hoang Bao
