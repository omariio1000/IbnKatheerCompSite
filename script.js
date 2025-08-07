const judgeData = {
  najeeb: {
    name: "Shaykh Mohamed Najeeb",
    bio: "Mohammed Najeeb has a Bachelors degree in Sharia (Islamic Law) from the esteemed Islamic University of Medinah. He also has a Masters degree and PhD from the College of Quran in the same University. He has Ijazat in the 10 modes of recitation from Sh. Ihab Fikri Haydar, muqri’ in the Prophet’s Masjid, and has studied with many top scholars in Saudi Arabia. Dr. Mohammed has taught Qira’at and Quranic sciences in the Islamic University of Medinah, and in the Prophetic Masjid in Medinah. He currently is an Imam in Sacramento, CA. He teaches with Zidni Islamic Institute.",
    image: "najeeb.jpg",
  },
  sharqawy: {
    name: "Shaykh Abdullah Sharqawy",
    bio: "Shaykh Abdullah Elsharkawy memorized the Qur'an by age 9 and holds a BA from Al-Azhar University. He has 11 Ijazaat in various Qira'at and a Master’s in Qur’anic Sciences. He is the Imam and Director of the Qur'an Program at MCYC Mosque in California. He serves as a judge in national and international Qur’an competitions, is a member of Al-Azhar's electronic Fatwa group, and belongs to several prestigious scholarly and Qur’anic bodies in Egypt.",
    image: "sharkawy.jpg",
  },
  wasil: {
    name: "Shaykh Wasil Jemal",
    bio: "Shaykh Wasil Jemal is a graduate of the Islamic University of Madinah’s College of Qur’an (2024), specializing in Qur’anic recitation and interpretation. He holds multiple qirā’āt and ijāzāt. Before Madinah, he memorized the Qur’an at a traditional madrasah and also earned a degree from Lewis & Clark College, combining traditional Islamic and Western academic education.",
    image: "wasil.jpg",
  },
  met: {
    name: "Muslim Educational Trust",
    bio: "In 1993, MET was founded with the dream to help create an open, empowering, and collaborative atmosphere within the Muslim community in the greater Portland area. Over the years, MET has made significant strides in the development of Portland‘s Islamic-based education. MET ’s focus on education through positive interaction with Muslims and non-Muslims and honest communication with the media and public officials has positively impacted not only the people of Portland, but well beyond our local area.",
    image: "sponsors/met.png",
    website: "https://www.metpdx.org/",
  },
  icch: {
    name: "Islamic Community Center of Hillsboro",
    bio: "The Islamic Community Center of Hillsboro was established in 2011 as a non for profit religious organization. Our goal is to establish a place of worship in the high tech corridor in Hillsboro based on the Islamic teaching and following the Quran and Sunna (way of life) of Prophet Mohammad peace be upon him.",
    image: "sponsors/icch.jpg",
    website: "https://www.icc-hillsboro.org/",
  },
  assaber: {
    name: "Masjid As-Saber (Islamic Center of Portland)",
    bio: "Established with the mission to provide a place of worship, education, and community support, Masjed Assaber serves as a vibrant hub for Muslims across the Portland region. Our mosque offers daily prayers, Jumu'ah prayers, and hosts a variety of religious, education, and social activities. We strive to foster a welcoming environment where everyone can deepen their faith, learn, and connect with others. Join us at Masjed Assaber and become a part of our growing family.",
    image: "sponsors/assaber.png",
    website: "https://www.assaber.org/",
  },
  bilal: {
    name: "Masjid Bilal",
    bio: "It is our honor and high privilege to welcome you to the Bilal Masjid Web site. It through the Gracious Mercy of Allah (SWT) that we are able to provide the few humble services for the community. Pray that Allah (SWT) guides us ALL in his Mercy and forgives us our transgressions.",
    image: "sponsors/bilal.png",
    website: "https://www.bilalmasjid.com/",
  },
  abubakr: {
    name: "Masjid Abu-Bakr",
    bio: "",
    image: "partners/abubakr.jpg",
    website: "https://masjidabubakarpdx.com/",
  },
  coolislam: {
    name: "Cool Islam",
    bio: "",
    image: "partners/coolislam.png",
    website: "https://coolislam.org/",
  },
  crescent: {
    name: "Crescent PDX Sports",
    bio: "",
    image: "partners/crescent.jpg",
    website: "https://www.crescentsportspdx.com/",
  },
  furqan: {
    name: "Masjid Al-Furqan",
    bio: "",
    image: "partners/furqan.jpg",
    website: "https://masjidfurqanpdx.org/",
  },
  hdf: {
    name: "Human Development Fund",
    bio: "",
    image: "partners/hdf.png",
    website: "https://hdfund.org/",
  },
  ibrahim: {
    name: "Masjid Ibrahim",
    bio: "",
    image: "partners/masjidibrahim.png",
    website: "https://masjid-ibrahim.com/",
  },
  isgp: {
    name: "Islamic Society of Greater Portland",
    bio: "",
    image: "partners/isgp.png",
    website: "https://isgponline.com/",
  },
  masportland: {
    name: "Muslim American Society - Portland",
    bio: "",
    image: "partners/mas.png",
    website: "https://www.facebook.com/MASPortland/",
  },
  towhid: {
    name: "Towhid Islamic Center",
    bio: "",
    image: "partners/towhid.jpg",
    website: "https://www.towhidic.org/",
  },
  nwdf: {
    name: "Northwest Dawah Foundation",
    bio: "",
    image: "partners/nwdawah.jpg",
    website: "https://www.facebook.com/nwdawahorg/",
  },
  oregondawah: {
    name: "Oregon Da'wah Initiative",
    bio: "",
    image: "partners/oregondawah.png",
    website: "https://www.oregondawah.org/",
  },
  osumsa: {
    name: "Oregon State University MSA",
    bio: "",
    image: "partners/osumsa.png",
    website: "https://www.instagram.com/osu.msa",
  },
  peaceaction: {
    name: "Peace Action Network",
    bio: "",
    image: "partners/peaceaction.jpg",
    website:
      "https://www.facebook.com/people/Peace-Action-Network/61560397760704/",
  },
  psumsa: {
    name: "Portland State University MSA",
    bio: "",
    image: "partners/pdxmsa.jpg",
    website: "https://www.instagram.com/pdxmsa",
  },
  upmsa: {
    name: "University of Portland MSA",
    bio: "",
    image: "partners/upmsa.jpg",
    website: "https://www.instagram.com/up.msa",
  },
  wmcc: {
    name: "Wilsonville Muslim Community Center",
    bio: "",
    image: "partners/wmcc.png",
    website: "https://www.wmccoregon.org/",
  },
  zain: {
    name: "Zain Institute",
    bio: "",
    image: "partners/zain.png",
    website: "",
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
      ${
        data.website
          ? `<p><a href="${data.website}" target="_blank" rel="noopener noreferrer">Visit Website</a></p>`
          : ""
      }
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
