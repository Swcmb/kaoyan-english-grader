FROM scratch

LABEL org.opencontainers.image.title="kaoyan-english-grader"
LABEL org.opencontainers.image.description="考研英语一、英语二六类主观题 AI 批改 Skill"
LABEL org.opencontainers.image.source="https://github.com/Swcmb/kaoyan-english-grader"
LABEL org.opencontainers.image.licenses="GPL-3.0-or-later"

COPY skills/kaoyan-english-grader/ /opt/skills/kaoyan-english-grader/
COPY LICENSE /licenses/LICENSE
