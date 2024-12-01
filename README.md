# Report Summarization for Course "Development of Employability and Entrepreneurship skills for Graduate Students" for THU Students

> Course Requirement: 总结报告“总字数不少于2000。总结分为面授、在线两部分，要求按每次课程分次书写，分别对应一段，内容不能是简单的课程笔记，而是能全面反映每次讲座的收获、心得体会及建议等”。

## Usage

1. Environment setup:

```bash
pip install -r requirements.txt
```

2. Collect documents and video recordings of the course.

    - Put the documents in `data/offline_files/`. Currently, the system supports `.docx` and `.txt` files. The file name should denote the name of the lecture.
    - To-do: Support for video summarization.
        - Currently, you can use `v2a.py` to convert video to audio, and then use ASR models to convert audio to text. Video files should be placed in `data/online_files/`. If the video is too long, you can split it into several parts and put them in the same folder. The file or folder name should denote the name of the lecture. The output audio files will be placed in `output/`.

3. Fill your `API key` in `llm_mapreduce/sum.yaml` and configure any other options you would like to. Run the following command to generate the report in `output/研究生素养课报告－姓名－学号－联系电话－Email地址.docx`: 

```bash
bash run.sh
```

## Acknowledgement

- [$\text{LLM}\times\text{MapReduce}$](https://github.com/thunlp/LLMxMapReduce)
- [OmAgent](https://github.com/om-ai-lab/OmAgent)
