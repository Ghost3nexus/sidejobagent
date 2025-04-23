'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Home, Briefcase, FileText, User, LogOut } from 'lucide-react';
import { Button } from '@/components/ui/button';

export default function Sidebar() {
  const pathname = usePathname();
  
  const isActive = (path: string) => {
    return pathname === path;
  };
  
  return (
    <div className="fixed inset-y-0 left-0 w-64 bg-sidebar border-r border-sidebar-border hidden lg:flex flex-col">
      <div className="p-6">
        <h1 className="text-xl font-bold text-sidebar-primary">副業マッチングAI</h1>
      </div>
      
      <nav className="flex-1 px-4 space-y-2">
        <Link href="/" passHref>
          <Button 
            variant={isActive('/') ? 'default' : 'ghost'} 
            className="w-full justify-start"
          >
            <Home className="mr-2 h-4 w-4" />
            ダッシュボード
          </Button>
        </Link>
        
        <Link href="/jobs" passHref>
          <Button 
            variant={isActive('/jobs') ? 'default' : 'ghost'} 
            className="w-full justify-start"
          >
            <Briefcase className="mr-2 h-4 w-4" />
            求人一覧
          </Button>
        </Link>
        
        <Link href="/profile" passHref>
          <Button 
            variant={isActive('/profile') ? 'default' : 'ghost'} 
            className="w-full justify-start"
          >
            <User className="mr-2 h-4 w-4" />
            プロフィール
          </Button>
        </Link>
        
        <Link href="/resume" passHref>
          <Button 
            variant={isActive('/resume') ? 'default' : 'ghost'} 
            className="w-full justify-start"
          >
            <FileText className="mr-2 h-4 w-4" />
            履歴書
          </Button>
        </Link>
      </nav>
      
      <div className="p-4 border-t border-sidebar-border">
        <Button variant="ghost" className="w-full justify-start text-sidebar-foreground hover:text-sidebar-primary">
          <LogOut className="mr-2 h-4 w-4" />
          ログアウト
        </Button>
      </div>
    </div>
  );
}
