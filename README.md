# Impacket-Obfuscated

**Advanced Obfuscated Version of Impacket - Bypass AV Detection**

> **⚠️ IMPORTANT NOTE**: This is a MODIFIED version of the original Impacket tool. All credit for the core functionality goes to the **Impacket Team (SecureAuth)**. This repository simply adds obfuscation to their original work for educational purposes.

## 🙏 Acknowledgments & Copyright

**This project is based on [Impacket](https://github.com/fortra/impacket) by SecureAuth**

- **Original Copyright**: SecureAuth Corporation and Impacket contributors
- **Original License**: Apache License 2.0
- **Modifications**: Only obfuscation/encryption layer added - NO core functionality changed

All credit for the underlying security tools, protocols, and functionality belongs to the **Impacket Team**. This repository is merely a proof-of-concept for obfuscation techniques and should not be seen as claiming ownership of their work.

### Original Impacket Team Contributors:
- SecureAuth Corporation
- Alberto Solino (@agsolino)
- All Impacket contributors

## 📋 Overview

This repository contains an **obfuscated/encrypted version of Impacket**, designed to bypass antivirus detection for authorized security testing. The original Impacket code has been transformed using the PyFortress Crypter to create runtime-protected Python files.

**What this is:**
- ✅ An obfuscation layer ON TOP of Impacket
- ✅ A proof-of-concept for code protection techniques
- ✅ For authorized security testing only

## 🔥 Latest Update

**Complete code replacement with working version** - All files have been obfuscated with random pronounceable names:

### File Renaming Examples (309 files obfuscated)

| Original File | Obfuscated Name |
|---------------|-----------------|
| `examples/CheckLDAPStatus.py` | `example/doxujodoxeq.py`
| `examples/DumpNTLMInfo.py`    | `example/jafuxeharume.py`
| `examples/Get-GPPPassword.py` | `example/hotahes.py`
| `examples/GetADComputers.py`  | `example/poripezoz.py`
| `examples/GetADUsers.py`      | `example/juxatojahuvu.py`
| `examples/GetLAPSPassword.py` | `example/sitibebovivu.py`
| `examples/GetNPUsers.py`      | `example/repodisahi.py`
| `examples/GetUserSPNs.py`     | `example/pibuku.py`
| `examples/addcomputer.py`     | `example/lokahutiwa.py`
| `examples/atexec.py`          | `example/hufoxolet.py`
| `examples/attrib.py`          | `example/fuhoquzu.py`
| `examples/badsuccessor.py`    | `example/tevinirega.py`
| `examples/changepasswd.py`    | `example/lewawo.py`
| `examples/checkMSSQLStatus.py`| `examples/wihekeda.py`
| `examples/dacledit.py`        | `example/cilepidohes.py`
| `examples/dcomexec.py`        | `example/jetaqoxawav.py`
| `examples/describeTicket.py`  | `example/qezedifiden.py`
| `examples/dpapi.py`           | `example/tagemijodubi.py`
| `examples/esentutl.py`        | `example/dexolocezes.py`
| `examples/exchanger.py`       | `example/caguzokuzam.py`
| `examples/filetime.py`        | `example/bukosilo.py`
| `examples/findDelegation.py`  | `example/vexuhoto.py`
| `examples/getArch.py`         | `example/ratuworewu.py`
| `examples/getPac.py`          | `example/tubuwe.py`
| `examples/getST.py`           | `example/kozufocuxiti.py`
| `examples/getTGT.py`          | `example/johurupaxev.py`
| `examples/goldenPac.py`       | `example/koquqequpile.py`
| `examples/karmaSMB.py`        | `example/qiqagapod.py`
| `examples/keylistattack.py`   | `example/bimiqutev.py`
| `examples/kintercept.py`      | `example/durolikejero.py`
| `examples/lookupsid.py`       | `example/kecuso.py`
| `examples/machine_role.py`    | `example/godoxumi.py`
| `examples/mimikatz.py`        | `example/fewujiz.py`
| `examples/mqtt_check.py`      | `example/jirabupeva.py`
| `examples/mssqlclient.py`     | `example/xoteha.py`
| `examples/mssqlinstance.py`   | `example/dilukof.py`
| `examples/net.py`             | `example/gewulem.py`
| `examples/netview.py`         | `example/kapoda.py`
| `examples/ntfs-read.py`       | `example/romafaxebof.py`
| `examples/ntlmrelayx.py`      | `example/jofilahuxil.py`
| `examples/owneredit.py`       | `example/kimikegev.py`
| `examples/ping.py`            | `example/cuhefe.py`
| `examples/ping6.py`           | `example/woganununaso.py`
| `examples/psexec.py`          | `example/nuvukenam.py`
| `examples/raiseChild.py`      | `example/cenirohapif.py`
| `examples/rbcd.py`            | `example/bugaqumoduk.py`
| `examples/rdp_check.py`       | `example/wajefatuzeh.py`
| `examples/reg.py`             | `example/xagupijepa.py`
| `examples/registry-read.py`   | `example/guxumuwepix.py`
| `examples/regsecrets.py`      | `example/pucatozot.py`
| `examples/rpcdump.py`         | `example/qizofudavi.py`
| `examples/rpcmap.py`          | `example/nibuzewefod.py`
| `examples/sambaPipe.py`       | `example/fovufipim.py`
| `examples/samedit.py`         | `example/xukote.py`
| `examples/samrdump.py`        | `example/xaperofubuw.py`
| `examples/secretsdump.py`     | `example/corujadevic.py`
| `examples/services.py`        | `example/qabemeda.py`
| `examples/smbclient.py`       | `example/vifuralun.py`
| `examples/smbexec.py`         | `example/tebumorexojo.py`
| `examples/smbserver.py`       | `example/vabezezeref.py`
| `examples/sniff.py`           | `example/bedulafoni.py`
| `examples/sniffer.py`         | `example/rarilutejo.py`
| `examples/split.py`           | `example/kuxihetoceju.py`
| `examples/ticketConverter.py` | `example/jadavil.py`
| `examples/ticketer.py`        | `example/zuvinel.py`
| `examples/tstool.py`          | `example/bezipi.py`
| `examples/wmiexec.py`         | `example/tificu.py`
| `examples/wmipersist.py`      | `example/tolovimetil.py`
| `examples/wmiquery.py`        | `example/tutava.py`
**All 309 Python files** have been renamed with random pronounceable names to avoid signature detection.


## 🚀 Features

- **Runtime Code Protection** - Compile → Marshal → Zlib → XOR → Base64 encryption pipeline
- **AV Evasion** - Bypasses signature-based detection (for authorized testing)
- **Dynamic File Renaming** - Random pronounceable module names (309 files renamed)
- **Anti-Analysis** - Junk code injection and random startup delays
- **Unique Hashes** - Different file hash on every compilation
- **Full Impacket Functionality** - All original features preserved (no credit taken)

## 📊 Obfuscation Statistics

- **Total Files Obfuscated**: 309 Python files
- **File Renaming**: 100% complete
- **Import Rewriting**: All imports updated to match new names
- **Code Encryption**: Every file individually encrypted with unique XOR keys

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/MrHarshvardhan/Impacket-Obfuscated.git
cd Impacket-Obfuscated

# Install dependencies
pip install -r requirements.txt

# Install the package
python setup.py install
