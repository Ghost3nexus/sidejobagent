'use client';

import { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";

interface ProfileFormData {
  fullName: string;
  jobTitle: string;
  skills: string;
  experience: string;
  education: string;
  preferredJobType: string;
  preferredCompensation: string;
}

export default function ProfileForm() {
  const [formData, setFormData] = useState<ProfileFormData>({
    fullName: '',
    jobTitle: '',
    skills: '',
    experience: '',
    education: '',
    preferredJobType: '',
    preferredCompensation: ''
  });
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    
    
    setIsLoading(false);
  };

  return (
    <Card className="w-full max-w-2xl mx-auto">
      <CardHeader>
        <CardTitle className="text-2xl font-bold">プロフィール設定</CardTitle>
        <CardDescription>
          あなたのスキルや経験を入力して、最適な副業案件を見つけましょう。
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="space-y-2">
            <Label htmlFor="fullName">氏名</Label>
            <Input 
              id="fullName" 
              name="fullName"
              value={formData.fullName}
              onChange={handleChange}
              required 
            />
          </div>
          
          <div className="space-y-2">
            <Label htmlFor="jobTitle">現在の職種</Label>
            <Input 
              id="jobTitle" 
              name="jobTitle"
              value={formData.jobTitle}
              onChange={handleChange}
              required 
            />
          </div>
          
          <div className="space-y-2">
            <Label htmlFor="skills">スキル（カンマ区切り）</Label>
            <Input 
              id="skills" 
              name="skills"
              value={formData.skills}
              onChange={handleChange}
              placeholder="例: JavaScript, React, Python"
              required 
            />
          </div>
          
          <div className="space-y-2">
            <Label htmlFor="experience">職務経験</Label>
            <textarea 
              id="experience" 
              name="experience"
              value={formData.experience}
              onChange={handleChange}
              className="w-full min-h-[100px] p-2 border border-input rounded-md focus:outline-none focus:ring-2 focus:ring-primary/30"
              placeholder="これまでの職務経験を記入してください"
              required 
            />
          </div>
          
          <div className="space-y-2">
            <Label htmlFor="education">学歴</Label>
            <Input 
              id="education" 
              name="education"
              value={formData.education}
              onChange={handleChange}
              required 
            />
          </div>
          
          <div className="space-y-2">
            <Label htmlFor="preferredJobType">希望する仕事タイプ</Label>
            <Input 
              id="preferredJobType" 
              name="preferredJobType"
              value={formData.preferredJobType}
              onChange={handleChange}
              placeholder="例: リモート, フリーランス, 週末のみ"
              required 
            />
          </div>
          
          <div className="space-y-2">
            <Label htmlFor="preferredCompensation">希望報酬（時給または月額）</Label>
            <Input 
              id="preferredCompensation" 
              name="preferredCompensation"
              value={formData.preferredCompensation}
              onChange={handleChange}
              placeholder="例: 5000円/時 または 20万円/月"
              required 
            />
          </div>
          
          <Button type="submit" className="w-full bg-primary hover:bg-primary/90" disabled={isLoading}>
            {isLoading ? '保存中...' : 'プロフィールを保存'}
          </Button>
        </form>
      </CardContent>
    </Card>
  );
}
