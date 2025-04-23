'use client';

import { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

interface Job {
  id: string;
  title: string;
  company: string;
  description: string;
  compensation: string;
  skills: string[];
  url: string;
}

export default function JobList() {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const mockJobs: Job[] = [
    {
      id: '1',
      title: 'フロントエンドエンジニア',
      company: 'テック株式会社',
      description: 'React/Next.jsを使用したWebアプリケーション開発',
      compensation: '6,000円/時',
      skills: ['React', 'Next.js', 'TypeScript'],
      url: 'https://example.com/job/1'
    },
    {
      id: '2',
      title: 'バックエンドエンジニア',
      company: 'デジタルソリューションズ',
      description: 'Python/FastAPIを使用したAPIサービス開発',
      compensation: '7,000円/時',
      skills: ['Python', 'FastAPI', 'PostgreSQL'],
      url: 'https://example.com/job/2'
    }
  ];

  useState(() => {
    setJobs(mockJobs);
  });

  return (
    <div className="container mx-auto py-8">
      <h1 className="text-3xl font-bold mb-6">求人一覧</h1>
      
      <div className="grid gap-6">
        {jobs.map((job) => (
          <Card key={job.id}>
            <CardHeader>
              <CardTitle>{job.title}</CardTitle>
              <CardDescription>{job.company}</CardDescription>
            </CardHeader>
            <CardContent>
              <p className="mb-2">{job.description}</p>
              <p className="font-semibold mb-2">報酬: {job.compensation}</p>
              <div className="flex flex-wrap gap-2 mb-4">
                {job.skills.map((skill) => (
                  <span 
                    key={skill} 
                    className="px-2 py-1 bg-blue-100 text-blue-800 rounded-full text-sm"
                  >
                    {skill}
                  </span>
                ))}
              </div>
              <div className="flex justify-end">
                <Button 
                  variant="outline" 
                  className="mr-2"
                  onClick={() => window.open(job.url, '_blank')}
                >
                  詳細を見る
                </Button>
                <Button>応募する</Button>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
