'use client';

import { useState, useEffect } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

interface Application {
  id: string;
  jobTitle: string;
  company: string;
  appliedDate: string;
  status: 'applied' | 'interviewing' | 'accepted' | 'rejected';
}

export default function ApplicationList() {
  const [applications, setApplications] = useState<Application[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    setTimeout(() => {
      setApplications([
        {
          id: '1',
          jobTitle: 'フロントエンドエンジニア',
          company: 'テック株式会社',
          appliedDate: '2025-04-15',
          status: 'interviewing'
        },
        {
          id: '2',
          jobTitle: 'バックエンドエンジニア',
          company: 'デジタルソリューションズ',
          appliedDate: '2025-04-10',
          status: 'applied'
        },
        {
          id: '3',
          jobTitle: 'UIデザイナー',
          company: 'クリエイティブスタジオ',
          appliedDate: '2025-04-05',
          status: 'rejected'
        }
      ]);
      setIsLoading(false);
    }, 1000);
    
    // 
  }, []);

  const getStatusBadge = (status: Application['status']) => {
    const statusConfig = {
      applied: { bg: 'bg-blue-100', text: 'text-blue-800', label: '応募済み' },
      interviewing: { bg: 'bg-yellow-100', text: 'text-yellow-800', label: '面接中' },
      accepted: { bg: 'bg-green-100', text: 'text-green-800', label: '採用' },
      rejected: { bg: 'bg-red-100', text: 'text-red-800', label: '不採用' }
    };
    
    const config = statusConfig[status];
    
    return (
      <span className={`px-2 py-1 ${config.bg} ${config.text} rounded-full text-xs`}>
        {config.label}
      </span>
    );
  };

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">応募履歴</h1>
      
      {isLoading ? (
        <p>読み込み中...</p>
      ) : applications.length === 0 ? (
        <Card>
          <CardContent className="pt-6">
            <p className="text-center text-gray-500">応募履歴がありません</p>
          </CardContent>
        </Card>
      ) : (
        <div className="space-y-4">
          {applications.map((application) => (
            <Card key={application.id}>
              <CardContent className="pt-6">
                <div className="flex flex-col md:flex-row md:items-center gap-4">
                  <div className="flex-1">
                    <h3 className="font-semibold">{application.jobTitle}</h3>
                    <p className="text-sm text-gray-600">{application.company}</p>
                    <p className="text-xs text-gray-500">応募日: {application.appliedDate}</p>
                  </div>
                  
                  <div className="flex items-center gap-4">
                    {getStatusBadge(application.status)}
                    
                    <Button variant="outline" size="sm">
                      詳細
                    </Button>
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}
