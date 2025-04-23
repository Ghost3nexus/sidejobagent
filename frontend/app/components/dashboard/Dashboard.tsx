'use client';

import { useState, useEffect } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Briefcase, FileText, User, TrendingUp } from 'lucide-react';
import Link from 'next/link';

interface DashboardStats {
  totalJobs: number;
  matchedJobs: number;
  applications: number;
  profileComplete: boolean;
}

export default function Dashboard() {
  const [stats, setStats] = useState<DashboardStats>({
    totalJobs: 0,
    matchedJobs: 0,
    applications: 0,
    profileComplete: false
  });
  
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    setTimeout(() => {
      setStats({
        totalJobs: 120,
        matchedJobs: 15,
        applications: 3,
        profileComplete: true
      });
      setIsLoading(false);
    }, 1000);
    
    // 
  }, []);

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">ダッシュボード</h1>
      
      {!stats.profileComplete && (
        <Card className="bg-yellow-50 border-yellow-200">
          <CardContent className="pt-6">
            <div className="flex items-center gap-4">
              <User className="h-8 w-8 text-yellow-500" />
              <div>
                <h3 className="text-lg font-semibold">プロフィールを完成させましょう</h3>
                <p className="text-sm text-gray-600">最適な求人マッチングのために、プロフィール情報を入力してください。</p>
              </div>
              <div className="ml-auto">
                <Link href="/profile" passHref>
                  <Button>プロフィールを編集</Button>
                </Link>
              </div>
            </div>
          </CardContent>
        </Card>
      )}
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-lg">求人総数</CardTitle>
            <CardDescription>利用可能な求人数</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex items-center">
              <Briefcase className="h-8 w-8 text-blue-500 mr-3" />
              <span className="text-3xl font-bold">
                {isLoading ? '...' : stats.totalJobs}
              </span>
            </div>
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-lg">マッチした求人</CardTitle>
            <CardDescription>あなたのスキルに合った求人</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex items-center">
              <TrendingUp className="h-8 w-8 text-green-500 mr-3" />
              <span className="text-3xl font-bold">
                {isLoading ? '...' : stats.matchedJobs}
              </span>
            </div>
            <div className="mt-4">
              <Link href="/jobs" passHref>
                <Button variant="outline" size="sm">求人を見る</Button>
              </Link>
            </div>
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-lg">応募履歴</CardTitle>
            <CardDescription>これまでの応募数</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex items-center">
              <FileText className="h-8 w-8 text-purple-500 mr-3" />
              <span className="text-3xl font-bold">
                {isLoading ? '...' : stats.applications}
              </span>
            </div>
            <div className="mt-4">
              <Link href="/applications" passHref>
                <Button variant="outline" size="sm">応募履歴を見る</Button>
              </Link>
            </div>
          </CardContent>
        </Card>
      </div>
      
      <Card>
        <CardHeader>
          <CardTitle>最近のマッチング求人</CardTitle>
          <CardDescription>あなたのスキルに最適な求人</CardDescription>
        </CardHeader>
        <CardContent>
          {isLoading ? (
            <p>読み込み中...</p>
          ) : (
            <div className="space-y-4">
              <div className="p-4 border rounded-lg">
                <h3 className="font-semibold">フロントエンドエンジニア</h3>
                <p className="text-sm text-gray-600">テック株式会社 • 6,000円/時</p>
                <div className="flex flex-wrap gap-2 my-2">
                  <span className="px-2 py-1 bg-blue-100 text-blue-800 rounded-full text-xs">React</span>
                  <span className="px-2 py-1 bg-blue-100 text-blue-800 rounded-full text-xs">Next.js</span>
                  <span className="px-2 py-1 bg-blue-100 text-blue-800 rounded-full text-xs">TypeScript</span>
                </div>
                <div className="flex justify-end">
                  <Button variant="outline" size="sm" className="mr-2">詳細</Button>
                  <Button size="sm">応募する</Button>
                </div>
              </div>
              
              <div className="p-4 border rounded-lg">
                <h3 className="font-semibold">バックエンドエンジニア</h3>
                <p className="text-sm text-gray-600">デジタルソリューションズ • 7,000円/時</p>
                <div className="flex flex-wrap gap-2 my-2">
                  <span className="px-2 py-1 bg-blue-100 text-blue-800 rounded-full text-xs">Python</span>
                  <span className="px-2 py-1 bg-blue-100 text-blue-800 rounded-full text-xs">FastAPI</span>
                  <span className="px-2 py-1 bg-blue-100 text-blue-800 rounded-full text-xs">PostgreSQL</span>
                </div>
                <div className="flex justify-end">
                  <Button variant="outline" size="sm" className="mr-2">詳細</Button>
                  <Button size="sm">応募する</Button>
                </div>
              </div>
              
              <div className="text-center mt-4">
                <Link href="/jobs" passHref>
                  <Button variant="link">すべての求人を見る →</Button>
                </Link>
              </div>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
