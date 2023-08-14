import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_TOKEN = os.getenv("API_TOKEN")
telegram_url = "https://api.telegram.org/file/bot{bot_token}/{file_path}"

prompts = [
    "A noblewoman’s portrait inspired by the works of Renaissance painter, Leonardo da Vinci, with soft chiaroscuro lighting and detailed fabric textures",
    "Frida Kahlo style self-portrait of a woman in traditional Mexican attire, holding a small monkey, amidst a lush tropical background",
    "A group portrait of a Victorian family in the style of John Singer Sargent, with rich fabrics, fine furniture, and a domestic interior setting",
    "Impressionist painting in the style of Claude Monet, a portrait of a young girl with a parasol standing in a sunlit garden",
    "Austrian Symbolism inspired portrait of a woman, influenced by Gustav Klimt’s ‘The Kiss’, shimmering with gold leaf detail and intricate patterns",
    "Black and white portrait of a grizzled old fisherman, inspired by the works of Sebastião Salgado, with intense contrast and fine detail",
    "Candid street portrait inspired by Vivian Maier, featuring a stylishly dressed woman in mid-century New York",
    "Close-up portrait of a ballerina in mid-performance, shot in the style of Lois Greenfield, with high motion and dramatic lighting",
    "An intimate portrait of a couple in love, shot in a sunlit forest, reminiscent of the warm and atmospheric style of Annie Leibovitz",
    "High contrast monochromatic portrait of a boxer after a fight, inspired by the sports photography of Neil Leifer",
]
