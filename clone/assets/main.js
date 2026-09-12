/* ============================================================
   Explorant — interactions
   - mobile nav toggle
   - sticky navbar "scrolled" state
   - scroll-reveal animations (IntersectionObserver)
   - render features / pricing / comparison (if containers exist)
   ============================================================ */
(function(){
  "use strict";

  /* ---- mobile hamburger ---- */
  const toggle = document.querySelector(".nav-toggle");
  const navR   = document.querySelector(".nav-r");
  if(toggle && navR){
    toggle.addEventListener("click", function(e){
      e.stopPropagation();
      this.classList.toggle("open");
      navR.classList.toggle("open");
    });
    document.addEventListener("click", function(){
      toggle.classList.remove("open");
      navR.classList.remove("open");
    });
  }

  /* ---- navbar shadow on scroll ---- */
  const nav = document.querySelector(".navbar");
  if(nav){
    const onScroll = () => nav.classList.toggle("scrolled", window.scrollY > 8);
    window.addEventListener("scroll", onScroll, {passive:true});
    onScroll();
  }

  /* ---- scroll-reveal ---- */
  const reveal = document.querySelectorAll("[data-reveal]");
  if("IntersectionObserver" in window && reveal.length){
    const io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(en.isIntersecting){ en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, {threshold:.12});
    reveal.forEach(function(el){
      el.style.cssText += ";opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s ease;";
      io.observe(el);
    });
  } else {
    reveal.forEach(function(el){ el.classList.add("in"); });
  }

  /* ---- render features ---- */
  const featBox = document.getElementById("features");
  if(featBox && typeof FEATS !== "undefined"){
    featBox.innerHTML = FEATS.map(function(f){
      return `<div class="feature" data-reveal><div class="ic">${icon(f[0])}</div>`+
             `<h4>${f[1]}</h4><p>${f[2]}</p></div>`;
    }).join("");
  }

  /* ---- render pricing ---- */
  const priceBox = document.getElementById("pricing");
  if(priceBox && typeof PLANS !== "undefined"){
    priceBox.innerHTML = PLANS.map(function(p){
      return `<div class="price" data-reveal>
        ${p.badge?`<span class="badge">${p.badge}</span>`:""}
        <div class="head">
          <div class="icon">${tier(p.color)}</div>
          <div class="name">${p.name}</div>
          <div class="amt">${p.price}<small>${p.per}</small></div>
          <div class="slots">${p.slots}</div>
        </div>
        <div class="body"><ul>${p.perks.map(function(x){return `<li>${x}</li>`;}).join("")}</ul>
          <a class="btn btn-outline" href="${p.cta}">Get It</a></div>
      </div>`;
    }).join("");
  }

  /* ---- render comparison ---- */
  const cmpBox = document.getElementById("cmp");
  if(cmpBox && typeof ROWS !== "undefined"){
    function cell(v){
      if(v===1) return `<td class="yes">✓</td>`;
      if(v===0) return `<td class="no">✗</td>`;
      return `<td>${v}</td>`;
    }
    cmpBox.innerHTML =
      `<thead><tr><th>Feature</th><th>Radiant</th><th>Ascendant</th><th>Silver</th></tr></thead>`+
      `<tbody>${ROWS.map(function(r){
        return `<tr><th>${r[0]}</th>${cell(r[1])}${cell(r[2])}${cell(r[3])}</tr>`;
      }).join("")}</tbody>`;
  }
})();
