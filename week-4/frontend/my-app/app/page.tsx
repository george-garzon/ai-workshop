import { HeroSection } from "./components/HeroSection";
import { Messenger } from "./components/Messenger";
import { SiteHeader } from "./components/SiteHeader";

export default function Home() {
  return (
    <main className="site-shell pt-[65px] min-[601px]:pt-[78px] min-[901px]:pt-0">
      <SiteHeader />
      <HeroSection />
      <Messenger />
    </main>
  );
}
