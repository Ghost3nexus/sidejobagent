'use client';

import { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export default function ResumeBuilder() {
  const [isGenerating, setIsGenerating] = useState<boolean>(false);
  const [resumeContent, setResumeContent] = useState<string>('');
  const [selectedJob, setSelectedJob] = useState<string>('');
  
  const handleGenerateResume = async () => {
    setIsGenerating(true);
    
    setTimeout(() => {
      setResumeContent(`# 職務経歴書

## 基本情報
- 氏名: 山田 太郎
- 職種: フロントエンドエンジニア
- 経験年数: 5年

## スキル
- 言語: JavaScript, TypeScript, HTML, CSS
- フレームワーク: React, Next.js, Vue.js
- ツール: Git, Webpack, Docker
- その他: レスポンシブデザイン, SEO対策, パフォーマンス最適化

## 職務経歴
### 株式会社テックソリューション (2020年4月 - 現在)
**シニアフロントエンドエンジニア**
- 大規模ECサイトのフロントエンド開発
- パフォーマンス最適化によるページ読み込み時間30%削減
- 新人エンジニアのメンタリングとコードレビュー

### 株式会社ウェブクリエイト (2018年1月 - 2020年3月)
**フロントエンドエンジニア**
- 複数のWebアプリケーション開発
- レスポンシブデザインの実装
- UI/UXの改善提案と実装

## 自己PR
フロントエンド開発において5年の経験を持ち、特にReactとNext.jsを用いた開発に強みがあります。パフォーマンス最適化やユーザビリティ向上に情熱を持って取り組んでいます。チーム開発においてはコミュニケーションを大切にし、技術的な課題解決だけでなく、プロジェクト全体の成功に貢献することを心がけています。

## 希望条件
- 勤務形態: リモートワーク
- 稼働時間: 週10-20時間
- 希望報酬: 6,000円/時`);
      setIsGenerating(false);
    }, 2000);
    
    //   
    //   
  };
  
  const handleDownloadPDF = () => {
    alert('PDFダウンロード機能は実装中です。');
  };
  
  const handleCopyToClipboard = () => {
    navigator.clipboard.writeText(resumeContent);
    alert('クリップボードにコピーしました！');
  };

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">履歴書ビルダー</h1>
      
      <Card>
        <CardHeader>
          <CardTitle>履歴書の生成</CardTitle>
          <CardDescription>
            プロフィール情報を元に、AIが最適な履歴書を生成します。
            特定の求人に合わせた履歴書を生成することもできます。
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="job-select">求人を選択（オプション）</Label>
              <select 
                id="job-select"
                className="w-full p-2 border rounded-md"
                value={selectedJob}
                onChange={(e) => setSelectedJob(e.target.value)}
              >
                <option value="">求人を選択せず一般的な履歴書を生成</option>
                <option value="1">フロントエンドエンジニア - テック株式会社</option>
                <option value="2">バックエンドエンジニア - デジタルソリューションズ</option>
              </select>
            </div>
            
            <Button 
              onClick={handleGenerateResume} 
              disabled={isGenerating}
              className="w-full"
            >
              {isGenerating ? '生成中...' : '履歴書を生成'}
            </Button>
          </div>
        </CardContent>
      </Card>
      
      {resumeContent && (
        <Card>
          <CardHeader>
            <CardTitle>生成された履歴書</CardTitle>
            <CardDescription>
              以下の履歴書をダウンロードまたはコピーして利用できます。
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="bg-gray-50 p-4 rounded-md whitespace-pre-wrap font-mono text-sm">
              {resumeContent}
            </div>
          </CardContent>
          <CardFooter className="flex justify-end space-x-2">
            <Button variant="outline" onClick={handleCopyToClipboard}>
              クリップボードにコピー
            </Button>
            <Button onClick={handleDownloadPDF}>
              PDFでダウンロード
            </Button>
          </CardFooter>
        </Card>
      )}
    </div>
  );
}
