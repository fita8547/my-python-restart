import React, { useMemo, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import {
  Home,
  MapPin,
  Search,
  MessageCircle,
  Heart,
  Plus,
  ChevronRight,
  ChevronLeft,
  Ellipsis,
  User,
  Camera,
  Send,
  Coins,
  Tag,
  Clock,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogFooter } from "@/components/ui/dialog";
import { Sheet, SheetContent, SheetHeader, SheetTitle, SheetTrigger } from "@/components/ui/sheet";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";

// --- Mock data --------------------------------------------------------------
const MOCK_PRODUCTS = [
  {
    id: 1,
    title: "아이폰 14 프로 256GB 퍼플",
    price: 1250000,
    location: "서초동",
    timeAgo: "1시간 전",
    likes: 14,
    chats: 3,
    thumb: "https://images.unsplash.com/photo-1603888894191-5d55c61c2f5b?q=80&w=1200&auto=format&fit=crop",
    desc:
      "케이스 씌워서만 사용한 A급 기기예요. 배터리 효율 92%, 구성품 사진 참고해주세요.",
    category: "디지털/가전",
    seller: { name: "민수", avatar: "https://i.pravatar.cc/150?img=12", rate: 4.8 },
  },
  {
    id: 2,
    title: "이케아 책상 MICKE 화이트",
    price: 40000,
    location: "잠실본동",
    timeAgo: "어제",
    likes: 7,
    chats: 5,
    thumb: "https://images.unsplash.com/photo-1519710164239-da123dc03ef4?q=80&w=1200&auto=format&fit=crop",
    desc:
      "이사 예정이라 급처해요. 상판 생활기스 조금 있고, 분해해드릴게요.",
    category: "가구/인테리어",
    seller: { name: "지우", avatar: "https://i.pravatar.cc/150?img=32", rate: 4.6 },
  },
  {
    id: 3,
    title: "나이키 덩크 로우 270mm",
    price: 65000,
    location: "삼성동",
    timeAgo: "2일 전",
    likes: 22,
    chats: 6,
    thumb: "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=1200&auto=format&fit=crop",
    desc:
      "실착 3회, 박스 O / 영수증 O. 직거래 선호합니다.",
    category: "생활/패션",
    seller: { name: "하린", avatar: "https://i.pravatar.cc/150?img=5", rate: 4.9 },
  },
];

const CATEGORIES = [
  "디지털/가전",
  "생활/패션",
  "가구/인테리어",
  "게임/취미",
  "유아동",
  "반려동물",
  "티켓/쿠폰",
];

// --- Utils ------------------------------------------------------------------
const formatPrice = (n) => n.toLocaleString("ko-KR") + "원";

// --- Small components -------------------------------------------------------
function AppHeader({ currentTown, onTownChange }) {
  return (
    <div className="sticky top-0 z-40 bg-white/80 backdrop-blur border-b">
      <div className="max-w-screen-sm mx-auto px-4 h-14 flex items-center justify-between">
        <button className="flex items-center gap-1 text-lg font-semibold">
          <MapPin className="w-5 h-5" />
          {currentTown}
          <ChevronDownMini />
        </button>
        <div className="flex items-center gap-2">
          <Button variant="ghost" size="icon" className="rounded-2xl">
            <Search className="w-5 h-5" />
          </Button>
          <Button variant="ghost" size="icon" className="rounded-2xl">
            <Ellipsis className="w-5 h-5" />
          </Button>
        </div>
      </div>
    </div>
  );
}

function ChevronDownMini() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M6 9l6 6 6-6" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}

function CategoryChips({ selected, onSelect }) {
  return (
    <div className="no-scrollbar overflow-x-auto flex gap-2 px-4 py-3 border-b bg-white">
      {CATEGORIES.map((c) => (
        <Badge
          key={c}
          variant={selected === c ? "default" : "secondary"}
          className="whitespace-nowrap rounded-2xl px-3 py-1 text-sm cursor-pointer"
          onClick={() => onSelect(selected === c ? null : c)}
        >
          {c}
        </Badge>
      ))}
    </div>
  );
}

function ProductCard({ item, onOpen }) {
  return (
    <Card className="rounded-2xl overflow-hidden hover:shadow-md transition cursor-pointer" onClick={() => onOpen(item)}>
      <div className="flex p-4 gap-4">
        <div className="relative w-28 h-28 shrink-0 rounded-xl overflow-hidden bg-gray-100">
          <img src={item.thumb} alt={item.title} className="object-cover w-full h-full" />
          <Badge className="absolute top-2 left-2 bg-black/70 text-white">{item.category}</Badge>
        </div>
        <div className="flex-1 min-w-0">
          <CardTitle className="text-base line-clamp-2 mb-1">{item.title}</CardTitle>
          <div className="text-lg font-bold mb-2">{formatPrice(item.price)}</div>
          <div className="flex items-center gap-2 text-sm text-muted-foreground">
            <span>{item.location}</span>
            <span>·</span>
            <span>{item.timeAgo}</span>
          </div>
          <div className="mt-2 flex items-center gap-3 text-sm text-muted-foreground">
            <span className="flex items-center gap-1"><MessageCircle className="w-4 h-4" />{item.chats}</span>
            <span className="flex items-center gap-1"><Heart className="w-4 h-4" />{item.likes}</span>
          </div>
        </div>
      </div>
    </Card>
  );
}

function BottomTabBar({ tab, setTab }) {
  const tabs = [
    { key: "home", label: "홈", icon: <Home className="w-5 h-5" /> },
    { key: "near", label: "동네생활", icon: <MapPin className="w-5 h-5" /> },
    { key: "chat", label: "채팅", icon: <MessageCircle className="w-5 h-5" /> },
    { key: "me", label: "나의 당근", icon: <User className="w-5 h-5" /> },
  ];
  return (
    <div className="sticky bottom-0 z-40 bg-white border-t">
      <div className="max-w-screen-sm mx-auto grid grid-cols-4 text-center">
        {tabs.map((t) => (
          <button
            key={t.key}
            onClick={() => setTab(t.key)}
            className={`flex flex-col items-center justify-center py-2 ${tab === t.key ? "text-orange-500" : "text-gray-600"}`}
          >
            {t.icon}
            <span className="text-xs mt-1">{t.label}</span>
          </button>
        ))}
      </div>
    </div>
  );
}

function NewItemForm({ onAdd }) {
  const [title, setTitle] = useState("");
  const [price, setPrice] = useState("");
  const [category, setCategory] = useState(CATEGORIES[0]);

  const canSubmit = title.trim().length > 1 && Number(price) > 0;

  return (
    <div className="space-y-3">
      <div className="space-y-2">
        <label className="text-sm text-muted-foreground">제목</label>
        <Input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="예) 다이슨 청소기 팝니다" />
      </div>
      <div className="space-y-2">
        <label className="text-sm text-muted-foreground">가격</label>
        <Input type="number" value={price} onChange={(e) => setPrice(e.target.value)} placeholder="숫자만 입력" />
      </div>
      <div className="space-y-2">
        <label className="text-sm text-muted-foreground">카테고리</label>
        <select className="w-full border rounded-md h-10 px-3" value={category} onChange={(e) => setCategory(e.target.value)}>
          {CATEGORIES.map((c) => (
            <option key={c} value={c}>{c}</option>
          ))}
        </select>
      </div>
      <Button className="w-full" disabled={!canSubmit} onClick={() => onAdd({ title, price: Number(price), category })}>
        <Plus className="w-4 h-4 mr-1" /> 등록하기
      </Button>
    </div>
  );
}

// --- Main Component ---------------------------------------------------------
export default function DanggeunClone() {
  const [town, setTown] = useState("잠실동");
  const [tab, setTab] = useState("home");
  const [category, setCategory] = useState(null);
  const [query, setQuery] = useState("");
  const [items, setItems] = useState(MOCK_PRODUCTS);
  const [active, setActive] = useState(null); // product for dialog
  const [chatOpen, setChatOpen] = useState(false);

  const filtered = useMemo(() => {
    return items.filter((i) => {
      const okCat = category ? i.category === category : true;
      const okQ = query.trim() ? i.title.toLowerCase().includes(query.toLowerCase()) : true;
      return okCat && okQ;
    });
  }, [items, category, query]);

  return (
    <div className="min-h-screen bg-neutral-50">
      <div className="max-w-screen-sm mx-auto">
        <AppHeader currentTown={town} onTownChange={setTown} />

        {/* Search */}
        <div className="px-4 py-3 flex gap-2 items-center bg-white border-b">
          <div className="relative flex-1">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
            <Input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="검색어를 입력하세요" className="pl-9 rounded-2xl" />
          </div>

          <Sheet>
            <SheetTrigger asChild>
              <Button variant="secondary" className="rounded-2xl">
                <Tag className="w-4 h-4 mr-1" /> 필터
              </Button>
            </SheetTrigger>
            <SheetContent side="right" className="w-[360px]">
              <SheetHeader>
                <SheetTitle>카테고리</SheetTitle>
              </SheetHeader>
              <div className="py-4 grid grid-cols-2 gap-2">
                {CATEGORIES.map((c) => (
                  <Button key={c} variant={category === c ? "default" : "outline"} onClick={() => setCategory(category === c ? null : c)} className="rounded-2xl">
                    {c}
                  </Button>
                ))}
              </div>
            </SheetContent>
          </Sheet>
        </div>

        <CategoryChips selected={category} onSelect={setCategory} />

        {/* Feed */}
        <div className="p-4 space-y-3">
          {filtered.map((p) => (
            <ProductCard key={p.id} item={p} onOpen={setActive} />
          ))}
          {filtered.length === 0 && (
            <Card className="rounded-2xl">
              <CardContent className="p-8 text-center text-muted-foreground">검색 결과가 없어요 😢</CardContent>
            </Card>
          )}
        </div>

        {/* Floating Action Button */}
        <Sheet>
          <SheetTrigger asChild>
            <Button size="icon" className="fixed bottom-20 right-4 rounded-full w-14 h-14 shadow-xl">
              <Plus className="w-6 h-6" />
            </Button>
          </SheetTrigger>
          <SheetContent className="w-[420px]">
            <SheetHeader>
              <SheetTitle>중고거래 글쓰기</SheetTitle>
            </SheetHeader>
            <div className="py-4 space-y-4">
              <div className="flex gap-2">
                <Button variant="outline" className="rounded-2xl">
                  <Camera className="w-4 h-4 mr-1" /> 사진 추가
                </Button>
                <Button variant="outline" className="rounded-2xl">
                  <MapPin className="w-4 h-4 mr-1" /> 위치
                </Button>
              </div>
              <NewItemForm
                onAdd={({ title, price, category }) => {
                  const newItem = {
                    id: Date.now(),
                    title,
                    price,
                    category,
                    location: town,
                    timeAgo: "방금 전",
                    likes: 0,
                    chats: 0,
                    thumb: "https://images.unsplash.com/photo-1518779578993-ec3579fee39f?q=80&w=1200&auto=format&fit=crop",
                    desc: `${title} 판매합니다. 직거래 선호해요!`,
                    seller: { name: "나", avatar: "https://i.pravatar.cc/150?img=67", rate: 4.7 },
                  };
                  setItems((prev) => [newItem, ...prev]);
                  alert("등록되었습니다!");
                }}
              />
            </div>
          </SheetContent>
        </Sheet>

        {/* Item Dialog */}
        <Dialog open={!!active} onOpenChange={(o) => !o && setActive(null)}>
          <DialogContent className="max-w-lg">
            {active && (
              <div className="space-y-4">
                <DialogHeader>
                  <DialogTitle className="text-xl">{active.title}</DialogTitle>
                </DialogHeader>

                <div className="aspect-video overflow-hidden rounded-xl bg-gray-100">
                  <img src={active.thumb} className="object-cover w-full h-full" alt={active.title} />
                </div>

                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <Avatar>
                      <AvatarImage src={active.seller.avatar} />
                      <AvatarFallback>U</AvatarFallback>
                    </Avatar>
                    <div>
                      <div className="font-semibold">{active.seller.name}</div>
                      <div className="text-sm text-muted-foreground">★ {active.seller.rate.toFixed(1)}</div>
                    </div>
                  </div>
                  <Badge variant="outline" className="rounded-2xl">{active.location}</Badge>
                </div>

                <div className="space-y-2">
                  <div className="text-2xl font-extrabold">{formatPrice(active.price)}</div>
                  <p className="text-sm text-muted-foreground leading-6">{active.desc}</p>
                  <div className="flex items-center gap-3 text-sm text-muted-foreground">
                    <span className="flex items-center gap-1"><Tag className="w-4 h-4" /> {active.category}</span>
                    <span className="flex items-center gap-1"><Clock className="w-4 h-4" /> {active.timeAgo}</span>
                  </div>
                </div>

                <DialogFooter className="sm:justify-between gap-2">
                  <Button variant="outline" onClick={() => setActive((a) => ({ ...a, likes: a.likes + 1 }))} className="rounded-2xl">
                    <Heart className="w-4 h-4 mr-1" /> 관심 {active.likes}
                  </Button>
                  <Button onClick={() => setChatOpen(true)} className="rounded-2xl">
                    <MessageCircle className="w-4 h-4 mr-1" /> 채팅하기
                  </Button>
                </DialogFooter>
              </div>
            )}
          </DialogContent>
        </Dialog>

        {/* Chat Sheet */}
        <Sheet open={chatOpen} onOpenChange={setChatOpen}>
          <SheetContent side="bottom" className="h-[65vh] max-w-screen-sm mx-auto">
            <SheetHeader>
              <SheetTitle>거래 채팅</SheetTitle>
            </SheetHeader>
            <ChatRoom product={active} onClose={() => setChatOpen(false)} />
          </SheetContent>
        </Sheet>

        <BottomTabBar tab={tab} setTab={setTab} />
      </div>
    </div>
  );
}

function ChatRoom({ product, onClose }) {
  const [msg, setMsg] = useState("");
  const [list, setList] = useState([
    { id: 1, mine: false, text: "안녕하세요! 아직 판매 중인가요?", time: "오후 2:10" },
    { id: 2, mine: true, text: "네, 가능합니다 :)", time: "오후 2:12" },
  ]);

  return (
    <div className="h-full flex flex-col">
      {product && (
        <Card className="rounded-2xl mb-3">
          <div className="flex items-center gap-3 p-3">
            <div className="w-12 h-12 rounded-lg overflow-hidden bg-gray-100">
              <img src={product.thumb} alt="thumb" className="w-full h-full object-cover" />
            </div>
            <div className="flex-1 min-w-0">
              <div className="text-sm truncate">{product.title}</div>
              <div className="font-semibold">{formatPrice(product.price)}</div>
            </div>
            <Button variant="ghost" size="icon" onClick={onClose}>
              <ChevronDownMini />
            </Button>
          </div>
        </Card>
      )}

      <div className="flex-1 overflow-y-auto space-y-2 px-1">
        {list.map((m) => (
          <div key={m.id} className={`flex ${m.mine ? "justify-end" : "justify-start"}`}>
            <div className={`max-w-[70%] px-3 py-2 rounded-2xl ${m.mine ? "bg-orange-100" : "bg-gray-100"}`}>
              <div className="text-sm leading-6">{m.text}</div>
              <div className="text-[10px] text-right text-muted-foreground mt-1">{m.time}</div>
            </div>
          </div>
        ))}
      </div>

      <div className="flex gap-2 pt-2">
        <Input value={msg} onChange={(e) => setMsg(e.target.value)} placeholder="메시지를 입력하세요" className="rounded-2xl" />
        <Button onClick={() => { if (!msg.trim()) return; setList((p) => [...p, { id: Date.now(), mine: true, text: msg, time: "지금" }]); setMsg(""); }}>
          <Send className="w-4 h-4" />
        </Button>
      </div>
    </div>
  );
}
