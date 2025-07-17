const judgeData = {
  najeeb: {
    name: "Shaykh Mohamed Najeeb",
    bio: "Mohammed Najeeb has a Bachelors degree in Sharia (Islamic Law) from the esteemed Islamic University of Medinah. He also has a Masters degree and PhD from the College of Quran in the same University. He has Ijazat in the 10 modes of recitation from Sh. Ihab Fikri Haydar, muqri’ in the Prophet’s Masjid, and has studied with many top scholars in Saudi Arabia. Dr. Mohammed has taught Qira’at and Quranic sciences in the Islamic University of Medinah, and in the Prophetic Masjid in Medinah. He currently is an Imam in Sacramento, CA. He teaches with Zidni Islamic Institute.",
    image: "judge1.jpg",
  },
  sharqawy: {
    name: "Shaykh Abdullah Sharqawy",
    bio: "Shaykh Abdullah Elsharkawy memorized the Qur'an by age 9 and holds a BA from Al-Azhar University. He has 11 Ijazaat in various Qira'at and a Master’s in Qur’anic Sciences. He is the Imam and Director of the Qur'an Program at MCYC Mosque in California. He serves as a judge in national and international Qur’an competitions, is a member of Al-Azhar's electronic Fatwa group, and belongs to several prestigious scholarly and Qur’anic bodies in Egypt.",
    image: "judge2.jpg",
  },
  wasil: {
    name: "Shaykh Wasil Jemal",
    bio: "Shaykh Wasil Jemal is a graduate of the Islamic University of Madinah’s College of Qur’an (2024), specializing in Qur’anic recitation and interpretation. He holds multiple qirā’āt and ijāzāt. Before Madinah, he memorized the Qur’an at a traditional madrasah and also earned a degree from Lewis & Clark College, combining traditional Islamic and Western academic education.",
    image: "judge3.jpg",
  },
};

function showJudgeCard(id) {
  const card = document.getElementById("judge-card");
  const info = document.getElementById("judge-info");
  const data = judgeData[id];
  if (data) {
    info.innerHTML = `
      <div class="judge-image-wrapper">
        <img src="${data.image}" alt="${data.name}" class="judge-image" />
      </div>
      <h3>${data.name}</h3>
      <p>${data.bio}</p>
    `;
    card.classList.remove("hidden");
  }
}

function closeJudgeCard() {
  document.getElementById("judge-card").classList.add("hidden");
}

document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") {
    closeJudgeCard();
  }
});

document.getElementById("judge-card").addEventListener("click", function (e) {
  if (e.target.id === "judge-card") {
    closeJudgeCard();
  }
});

function scrollToNextSection() {
  const aboutSection = document.querySelector("#about");
  if (aboutSection) {
    aboutSection.scrollIntoView({ behavior: "smooth" });
  }
}

window.addEventListener("scroll", () => {
  const btn = document.getElementById("scroll-down-btn");
  const homeSection = document.querySelector("#home");

  if (!btn || !homeSection) return;

  const homeBottom = homeSection.getBoundingClientRect().bottom;

  // Show button only when user is in the #home section
  if (homeBottom > window.innerHeight / 2) {
    btn.classList.remove("hidden");
  } else {
    btn.classList.add("hidden");
  }
});
