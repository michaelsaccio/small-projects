# Cover Letter Generator

This project utilizes OpenAI's GPT-3.5-turbo model to generate impressive cover letters tailored to job requirements. The process involves importing API keys and prompting files, creating an assistant, and building a strong prompt for cover letter generation, that is formatted and saved as a PDF

## Motivation

Crafting personalized cover letters for job applications is a time-consuming process, demanding tailored content that aligns with specific job descriptions. While leveraging ChatGPT offers a practical solution, it comes with the challenge of repeatedly inputting experiences, formatting requests, and job descriptions for every new letter. Additionally, expecting the model to retain past information is not feasible.

The traditional approach involves juggling multiple documents or meticulously editing ChatGPT's responses, leading to a cumbersome workflow. Recognizing this inefficiency, this script streamlines the cover letter generation process. It predefines a detailed and effective prompt, emphasizing relevant experiences in relation to job requirements. Moreover, the script stores your experience and formatting preferences in separate files, eliminating the need for repeated manual input.

With this script, the only input required is the job description, saving valuable time by eliminating the need for repetitive prompting and downloading. It offers a more efficient and user-friendly way to harness the power of ChatGPT for crafting impactful cover letters tailored to specific job opportunities.

## Usage

1. Store your API key in a file named `api_key.txt`.
2. Prepare the template, work experience, and job description in separate text files (`template.txt`, `work_exp.txt`, `job_description.txt`).
3. Run the script to interact with the GPT-3.5-turbo model and generate a customized cover letter as a PDF.

## Steps

1. Import API key and prompting files.
2. Insert the API key and initialize the OpenAI client.
3. Create an assistant for cover letter generation.
4. Build a strong prompt, focusing on skills and experiences matching job requirements.
5. Assign run components for the assistant to generate the cover letter.
6. Monitor and print updates on the assistant's progress until completion.
7. Extract the generated cover letter.

Ensure that you have the necessary permissions to use the OpenAI API and have the required files in the specified format before running the script.
