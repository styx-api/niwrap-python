# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__FS_ROI_LABEL_METADATA = Metadata(
    id="a7302764b06fe1cdcf5b431a5db63243d5a576e3.boutiques",
    name="@FS_roi_label",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VFsRoiLabelParameters = typing.TypedDict('VFsRoiLabelParameters', {
    "__STYXTYPE__": typing.Literal["@FS_roi_label"],
    "label_int": typing.NotRequired[float | None],
    "lab_flag": typing.NotRequired[float | None],
    "rank_int": typing.NotRequired[float | None],
    "rankmap_file": typing.NotRequired[InputPathType | None],
    "name": typing.NotRequired[str | None],
    "labeltable_file": typing.NotRequired[InputPathType | None],
    "surf_annot_cmap": typing.NotRequired[InputPathType | None],
    "slab_int": typing.NotRequired[float | None],
    "sname_name": typing.NotRequired[str | None],
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
        "@FS_roi_label": v__fs_roi_label_cargs,
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


class VFsRoiLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__fs_roi_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__fs_roi_label_params(
    label_int: float | None = None,
    lab_flag: float | None = None,
    rank_int: float | None = None,
    rankmap_file: InputPathType | None = None,
    name: str | None = None,
    labeltable_file: InputPathType | None = None,
    surf_annot_cmap: InputPathType | None = None,
    slab_int: float | None = None,
    sname_name: str | None = None,
) -> VFsRoiLabelParameters:
    """
    Build parameters.
    
    Args:
        label_int: Integer labeled area in FreeSurfer's parcellation.
        lab_flag: Return the name of an integer labeled area in FreeSurfer's\
            parcellation.
        rank_int: Return the name of ranked integer labeled area from the\
            output of 3dRank or 3dmerge -1rank.
        rankmap_file: Path to the rank map file.
        name: Return entries matching NAME (case insensitive, partial match)\
            from FreeSurfer's FreeSurferColorLUT.txt.
        labeltable_file: Path to the label table file.
        surf_annot_cmap: CMAP file output by FSread_annot's -roi_1D option.
        slab_int: Return the name of an integer labeled area in FreeSurfer's\
            surface-based annotation.
        sname_name: Return the entries matching NAME (case insensitive, partial\
            match) from the CMAP file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@FS_roi_label",
    }
    if label_int is not None:
        params["label_int"] = label_int
    if lab_flag is not None:
        params["lab_flag"] = lab_flag
    if rank_int is not None:
        params["rank_int"] = rank_int
    if rankmap_file is not None:
        params["rankmap_file"] = rankmap_file
    if name is not None:
        params["name"] = name
    if labeltable_file is not None:
        params["labeltable_file"] = labeltable_file
    if surf_annot_cmap is not None:
        params["surf_annot_cmap"] = surf_annot_cmap
    if slab_int is not None:
        params["slab_int"] = slab_int
    if sname_name is not None:
        params["sname_name"] = sname_name
    return params


def v__fs_roi_label_cargs(
    params: VFsRoiLabelParameters,
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
    cargs.append("@FS_roi_label")
    if params.get("label_int") is not None:
        cargs.append(str(params.get("label_int")))
    if params.get("lab_flag") is not None:
        cargs.extend([
            "-lab",
            str(params.get("lab_flag"))
        ])
    if params.get("rank_int") is not None:
        cargs.extend([
            "-rank",
            str(params.get("rank_int"))
        ])
    if params.get("rankmap_file") is not None:
        cargs.extend([
            "-rankmap",
            execution.input_file(params.get("rankmap_file"))
        ])
    if params.get("name") is not None:
        cargs.extend([
            "-name",
            params.get("name")
        ])
    if params.get("labeltable_file") is not None:
        cargs.extend([
            "-labeltable",
            execution.input_file(params.get("labeltable_file"))
        ])
    if params.get("surf_annot_cmap") is not None:
        cargs.extend([
            "-surf_annot_cmap",
            execution.input_file(params.get("surf_annot_cmap"))
        ])
    if params.get("slab_int") is not None:
        cargs.extend([
            "-slab",
            str(params.get("slab_int"))
        ])
    if params.get("sname_name") is not None:
        cargs.extend([
            "-sname",
            params.get("sname_name")
        ])
    return cargs


def v__fs_roi_label_outputs(
    params: VFsRoiLabelParameters,
    execution: Execution,
) -> VFsRoiLabelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VFsRoiLabelOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__fs_roi_label_execute(
    params: VFsRoiLabelParameters,
    execution: Execution,
) -> VFsRoiLabelOutputs:
    """
    Tool to get labels associated with FreeSurfer's parcellation and annotation
    files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VFsRoiLabelOutputs`).
    """
    params = execution.params(params)
    cargs = v__fs_roi_label_cargs(params, execution)
    ret = v__fs_roi_label_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__fs_roi_label(
    label_int: float | None = None,
    lab_flag: float | None = None,
    rank_int: float | None = None,
    rankmap_file: InputPathType | None = None,
    name: str | None = None,
    labeltable_file: InputPathType | None = None,
    surf_annot_cmap: InputPathType | None = None,
    slab_int: float | None = None,
    sname_name: str | None = None,
    runner: Runner | None = None,
) -> VFsRoiLabelOutputs:
    """
    Tool to get labels associated with FreeSurfer's parcellation and annotation
    files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        label_int: Integer labeled area in FreeSurfer's parcellation.
        lab_flag: Return the name of an integer labeled area in FreeSurfer's\
            parcellation.
        rank_int: Return the name of ranked integer labeled area from the\
            output of 3dRank or 3dmerge -1rank.
        rankmap_file: Path to the rank map file.
        name: Return entries matching NAME (case insensitive, partial match)\
            from FreeSurfer's FreeSurferColorLUT.txt.
        labeltable_file: Path to the label table file.
        surf_annot_cmap: CMAP file output by FSread_annot's -roi_1D option.
        slab_int: Return the name of an integer labeled area in FreeSurfer's\
            surface-based annotation.
        sname_name: Return the entries matching NAME (case insensitive, partial\
            match) from the CMAP file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VFsRoiLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__FS_ROI_LABEL_METADATA)
    params = v__fs_roi_label_params(
        label_int=label_int,
        lab_flag=lab_flag,
        rank_int=rank_int,
        rankmap_file=rankmap_file,
        name=name,
        labeltable_file=labeltable_file,
        surf_annot_cmap=surf_annot_cmap,
        slab_int=slab_int,
        sname_name=sname_name,
    )
    return v__fs_roi_label_execute(params, execution)


__all__ = [
    "VFsRoiLabelOutputs",
    "VFsRoiLabelParameters",
    "V__FS_ROI_LABEL_METADATA",
    "v__fs_roi_label",
    "v__fs_roi_label_params",
]
