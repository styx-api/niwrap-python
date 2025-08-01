# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DCMSPLIT_METADATA = Metadata(
    id="32509a30d18a74c8ffaec50695d2c1f51a6cff31.boutiques",
    name="dcmsplit",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


DcmsplitParameters = typing.TypedDict('DcmsplitParameters', {
    "__STYXTYPE__": typing.Literal["dcmsplit"],
    "dcm_dir": str,
    "out_dir": str,
    "copy": bool,
    "link": bool,
    "split_name": bool,
    "split_uid": bool,
    "series_no": bool,
    "series_plus": bool,
    "dicom_tag": typing.NotRequired[str | None],
    "study_description": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "dcmsplit": dcmsplit_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class DcmsplitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dcmsplit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dcmsplit_params(
    dcm_dir: str,
    out_dir: str,
    copy_: bool = False,
    link: bool = False,
    split_name: bool = False,
    split_uid: bool = False,
    series_no: bool = False,
    series_plus: bool = False,
    dicom_tag: str | None = None,
    study_description: bool = False,
) -> DcmsplitParameters:
    """
    Build parameters.
    
    Args:
        dcm_dir: Directory containing the DICOM files.
        out_dir: Output directory for split DICOM files.
        copy_: Copy files instead of creating symbolic links.
        link: Link files instead of copying (default behavior).
        split_name: Split files by patient name instead of UID.
        split_uid: Split files by Study UID instead of name (default behavior).
        series_no: Split files by series number.
        series_plus: Split files by series number and either name or UID.
        dicom_tag: Split files by given DICOM tag (group element).
        study_description: Split files by Study Description.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dcmsplit",
        "dcm_dir": dcm_dir,
        "out_dir": out_dir,
        "copy": copy_,
        "link": link,
        "split_name": split_name,
        "split_uid": split_uid,
        "series_no": series_no,
        "series_plus": series_plus,
        "study_description": study_description,
    }
    if dicom_tag is not None:
        params["dicom_tag"] = dicom_tag
    return params


def dcmsplit_cargs(
    params: DcmsplitParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("dcmsplit")
    cargs.extend([
        "--dcm",
        params.get("dcm_dir")
    ])
    cargs.extend([
        "--o",
        params.get("out_dir")
    ])
    if params.get("copy"):
        cargs.append("--cp")
    if params.get("link"):
        cargs.append("--link")
    if params.get("split_name"):
        cargs.append("--name")
    if params.get("split_uid"):
        cargs.append("--uid")
    if params.get("series_no"):
        cargs.append("--seriesno")
    if params.get("series_plus"):
        cargs.append("--series+")
    if params.get("dicom_tag") is not None:
        cargs.extend([
            "--t",
            params.get("dicom_tag")
        ])
    if params.get("study_description"):
        cargs.append("--studyDes")
    return cargs


def dcmsplit_outputs(
    params: DcmsplitParameters,
    execution: Execution,
) -> DcmsplitOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DcmsplitOutputs(
        root=execution.output_file("."),
    )
    return ret


def dcmsplit_execute(
    params: DcmsplitParameters,
    execution: Execution,
) -> DcmsplitOutputs:
    """
    Splits DICOM files into separate folders based on a unique identifier (UID).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DcmsplitOutputs`).
    """
    params = execution.params(params)
    cargs = dcmsplit_cargs(params, execution)
    ret = dcmsplit_outputs(params, execution)
    execution.run(cargs)
    return ret


def dcmsplit(
    dcm_dir: str,
    out_dir: str,
    copy_: bool = False,
    link: bool = False,
    split_name: bool = False,
    split_uid: bool = False,
    series_no: bool = False,
    series_plus: bool = False,
    dicom_tag: str | None = None,
    study_description: bool = False,
    runner: Runner | None = None,
) -> DcmsplitOutputs:
    """
    Splits DICOM files into separate folders based on a unique identifier (UID).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        dcm_dir: Directory containing the DICOM files.
        out_dir: Output directory for split DICOM files.
        copy_: Copy files instead of creating symbolic links.
        link: Link files instead of copying (default behavior).
        split_name: Split files by patient name instead of UID.
        split_uid: Split files by Study UID instead of name (default behavior).
        series_no: Split files by series number.
        series_plus: Split files by series number and either name or UID.
        dicom_tag: Split files by given DICOM tag (group element).
        study_description: Split files by Study Description.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DcmsplitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCMSPLIT_METADATA)
    params = dcmsplit_params(
        dcm_dir=dcm_dir,
        out_dir=out_dir,
        copy_=copy_,
        link=link,
        split_name=split_name,
        split_uid=split_uid,
        series_no=series_no,
        series_plus=series_plus,
        dicom_tag=dicom_tag,
        study_description=study_description,
    )
    return dcmsplit_execute(params, execution)


__all__ = [
    "DCMSPLIT_METADATA",
    "DcmsplitOutputs",
    "DcmsplitParameters",
    "dcmsplit",
    "dcmsplit_params",
]
