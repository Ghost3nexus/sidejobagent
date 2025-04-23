import os
from typing import Dict, Any, List, Optional
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

class LLMService:
    """Service for interacting with language models"""
    
    def __init__(self):
        """Initialize the LLM service with OpenAI"""
        self.llm = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.7,
            model_name="gpt-4o"
        )
    
    def generate_resume(self, profile_data: Dict[str, Any], job_data: Optional[Dict[str, Any]] = None) -> str:
        """Generate a resume based on profile data and optionally job data"""
        
        if job_data:
            template = """
            あなたはプロフェッショナルな履歴書作成者です。以下のプロフィール情報と求人情報を元に、
            日本語で最適な職務経歴書を作成してください。

            職種: {job_type}
            スキル: {skills}
            希望報酬: {desired_compensation}
            希望勤務時間: {work_hours}

            タイトル: {job_title}
            説明: {job_description}
            必要スキル: {job_skills}
            
            職務経歴書は以下の形式で作成してください：
            1. 基本情報
            2. スキル
            3. 職務経歴
            4. 自己PR
            5. 希望条件
            
            マークダウン形式で出力してください。
            """
            
            prompt = PromptTemplate(
                input_variables=["job_type", "skills", "desired_compensation", "work_hours", 
                                "job_title", "job_description", "job_skills"],
                template=template
            )
            
            input_data = {
                "job_type": profile_data.get("job_type", ""),
                "skills": ", ".join(profile_data.get("skills", [])),
                "desired_compensation": profile_data.get("desired_compensation", ""),
                "work_hours": profile_data.get("work_hours", ""),
                "job_title": job_data.get("title", ""),
                "job_description": job_data.get("description", ""),
                "job_skills": ", ".join(job_data.get("skills", []))
            }
        else:
            template = """
            あなたはプロフェッショナルな履歴書作成者です。以下のプロフィール情報を元に、
            日本語で最適な職務経歴書を作成してください。

            職種: {job_type}
            スキル: {skills}
            希望報酬: {desired_compensation}
            希望勤務時間: {work_hours}
            
            職務経歴書は以下の形式で作成してください：
            1. 基本情報
            2. スキル
            3. 職務経歴
            4. 自己PR
            5. 希望条件
            
            マークダウン形式で出力してください。
            """
            
            prompt = PromptTemplate(
                input_variables=["job_type", "skills", "desired_compensation", "work_hours"],
                template=template
            )
            
            input_data = {
                "job_type": profile_data.get("job_type", ""),
                "skills": ", ".join(profile_data.get("skills", [])),
                "desired_compensation": profile_data.get("desired_compensation", ""),
                "work_hours": profile_data.get("work_hours", "")
            }
        
        chain = LLMChain(llm=self.llm, prompt=prompt)
        result = chain.run(**input_data)
        
        return result
    
    def generate_cover_letter(self, profile_data: Dict[str, Any], job_data: Dict[str, Any]) -> str:
        """Generate a cover letter based on profile data and job data"""
        
        template = """
        あなたはプロフェッショナルな応募文書作成者です。以下のプロフィール情報と求人情報を元に、
        日本語で最適な応募文（カバーレター）を作成してください。

        職種: {job_type}
        スキル: {skills}
        希望報酬: {desired_compensation}
        希望勤務時間: {work_hours}

        タイトル: {job_title}
        説明: {job_description}
        必要スキル: {job_skills}
        
        応募文は以下の形式で作成してください：
        1. 挨拶
        2. 自己紹介と応募理由
        3. 関連スキルと経験のアピール
        4. 求人内容への関心表明
        5. 締めの挨拶
        
        マークダウン形式で出力してください。
        """
        
        prompt = PromptTemplate(
            input_variables=["job_type", "skills", "desired_compensation", "work_hours", 
                            "job_title", "job_description", "job_skills"],
            template=template
        )
        
        input_data = {
            "job_type": profile_data.get("job_type", ""),
            "skills": ", ".join(profile_data.get("skills", [])),
            "desired_compensation": profile_data.get("desired_compensation", ""),
            "work_hours": profile_data.get("work_hours", ""),
            "job_title": job_data.get("title", ""),
            "job_description": job_data.get("description", ""),
            "job_skills": ", ".join(job_data.get("skills", []))
        }
        
        chain = LLMChain(llm=self.llm, prompt=prompt)
        result = chain.run(**input_data)
        
        return result
    
    def calculate_job_match_score(self, profile_data: Dict[str, Any], job_data: Dict[str, Any]) -> float:
        """Calculate a match score between a user profile and a job"""
        
        template = """
        あなたは求人マッチングの専門家です。以下のプロフィール情報と求人情報を元に、
        0から1の間のマッチングスコアを計算してください。

        職種: {job_type}
        スキル: {skills}
        希望報酬: {desired_compensation}
        希望勤務時間: {work_hours}

        タイトル: {job_title}
        説明: {job_description}
        報酬: {job_compensation}
        必要スキル: {job_skills}
        
        スキルの一致度、職種の一致度、報酬の一致度、勤務時間の一致度を考慮して、
        0から1の間の数値でマッチングスコアを出力してください。
        出力は数値のみにしてください。
        """
        
        prompt = PromptTemplate(
            input_variables=["job_type", "skills", "desired_compensation", "work_hours", 
                            "job_title", "job_description", "job_compensation", "job_skills"],
            template=template
        )
        
        input_data = {
            "job_type": profile_data.get("job_type", ""),
            "skills": ", ".join(profile_data.get("skills", [])),
            "desired_compensation": profile_data.get("desired_compensation", ""),
            "work_hours": profile_data.get("work_hours", ""),
            "job_title": job_data.get("title", ""),
            "job_description": job_data.get("description", ""),
            "job_compensation": job_data.get("compensation", ""),
            "job_skills": ", ".join(job_data.get("skills", []))
        }
        
        chain = LLMChain(llm=self.llm, prompt=prompt)
        result = chain.run(**input_data)
        
        try:
            score = float(result.strip())
            score = max(0.0, min(1.0, score))
            return score
        except ValueError:
            return 0.5

llm_service = LLMService()
