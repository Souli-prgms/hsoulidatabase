from hsoulidatabase.database import Database
import hsoulidatabase.utils as utils
import argparse


def update_database(build_path, extract_path, edits_path, output_path):
    build = utils.get_json_data(build_path)
    extract = utils.get_json_data(extract_path)
    edits = utils.get_json_data(edits_path)

    status = {}
    if len(build) > 0:
        # Build graph
        db = Database(build[0][0])
        if len(build) > 1:
            db.add_nodes(build[1:])
        # Add extract
        db.add_extract(extract)
        # Graph edits
        db.add_nodes(edits)
        # Update status
        status = db.get_extract_status()

    utils.write_status(status, output_path)


def main():
    parser = argparse.ArgumentParser(description='Update database')
    parser.add_argument('build_path', type=str, help='Build path')
    parser.add_argument('extract_path', type=str, help='Extract path')
    parser.add_argument('edits_path', type=str, help='Edits path')
    parser.add_argument('output_path', type=str, help='Output path (path + name)')

    args = parser.parse_args()
    update_database(**vars(args))


if __name__ == "__main__":
    main()