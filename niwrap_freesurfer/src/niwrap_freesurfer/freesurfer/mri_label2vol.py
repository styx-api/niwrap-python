# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_LABEL2VOL_METADATA = Metadata(
    id="cd26e42611cf3dfd2ed0aa17d46d76686633fdae.boutiques",
    name="mri_label2vol",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriLabel2volParameters = typing.TypedDict('MriLabel2volParameters', {
    "__STYXTYPE__": typing.Literal["mri_label2vol"],
    "labels": typing.NotRequired[list[str] | None],
    "annotation": typing.NotRequired[InputPathType | None],
    "segmentation": typing.NotRequired[InputPathType | None],
    "template": InputPathType,
    "registration": typing.NotRequired[InputPathType | None],
    "identity_flag": bool,
    "fill_threshold": typing.NotRequired[float | None],
    "label_vox_vol": typing.NotRequired[float | None],
    "projection": typing.NotRequired[str | None],
    "subject": typing.NotRequired[str | None],
    "hemisphere": typing.NotRequired[str | None],
    "output_volume": str,
    "hits_volume": typing.NotRequired[str | None],
    "label_stat_volume": typing.NotRequired[str | None],
    "stat_threshold": typing.NotRequired[float | None],
    "offset": typing.NotRequired[float | None],
    "defects": typing.NotRequired[str | None],
    "native_vox2ras_flag": bool,
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
        "mri_label2vol": mri_label2vol_cargs,
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
        "mri_label2vol": mri_label2vol_outputs,
    }.get(t)


class MriLabel2volOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_label2vol(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_vol: OutputPathType
    """The output volume where each voxel has the label it's assigned to."""
    hits_vol: OutputPathType | None
    """The hit volume file showing number of hits per voxel."""
    label_stat_vol: OutputPathType | None
    """The label stat volume file."""


def mri_label2vol_params(
    template: InputPathType,
    output_volume: str,
    labels: list[str] | None = None,
    annotation: InputPathType | None = None,
    segmentation: InputPathType | None = None,
    registration: InputPathType | None = None,
    identity_flag: bool = False,
    fill_threshold: float | None = None,
    label_vox_vol: float | None = None,
    projection: str | None = None,
    subject: str | None = None,
    hemisphere: str | None = None,
    hits_volume: str | None = None,
    label_stat_volume: str | None = None,
    stat_threshold: float | None = None,
    offset: float | None = None,
    defects: str | None = None,
    native_vox2ras_flag: bool = False,
) -> MriLabel2volParameters:
    """
    Build parameters.
    
    Args:
        template: Template volume; the output will have the same size and\
            geometry.
        output_volume: Output volume in which each voxel will have the number\
            of the label to which it is assigned.
        labels: Enter the name of the label file. For multiple labels, use\
            multiple --label flags.
        annotation: Surface annotation file. Use this to input annotations\
            directly.
        segmentation: Path to input segmentation.
        registration: tkregister-style registration matrix mapping LabelXYZ to\
            VolXYZ.
        identity_flag: Use the identity matrix as the registration.
        fill_threshold: Threshold for voxel fill; a value between 0 and 1.
        label_vox_vol: Volume of each label point; default is 1mm³.
        projection: Project the label along the surface normal. Type can be abs\
            or frac.
        subject: FREESURFER subject identifier; needed with --proj.
        hemisphere: Hemisphere to use for --proj or --annot. Legal values are\
            lh and rh.
        hits_volume: Hit volume, a multi-frame volume with one frame per label\
            showing the number of hits per voxel.
        label_stat_volume: Map the label stats field into the volume.
        stat_threshold: Only use label point where stat > thresh.
        offset: Add offset to the segmentation numbers.
        defects: Creates a segmentation volume of the surface defects.
        native_vox2ras_flag: Use native voxel-to-RAS transform instead of\
            tkregister-style.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_label2vol",
        "template": template,
        "identity_flag": identity_flag,
        "output_volume": output_volume,
        "native_vox2ras_flag": native_vox2ras_flag,
    }
    if labels is not None:
        params["labels"] = labels
    if annotation is not None:
        params["annotation"] = annotation
    if segmentation is not None:
        params["segmentation"] = segmentation
    if registration is not None:
        params["registration"] = registration
    if fill_threshold is not None:
        params["fill_threshold"] = fill_threshold
    if label_vox_vol is not None:
        params["label_vox_vol"] = label_vox_vol
    if projection is not None:
        params["projection"] = projection
    if subject is not None:
        params["subject"] = subject
    if hemisphere is not None:
        params["hemisphere"] = hemisphere
    if hits_volume is not None:
        params["hits_volume"] = hits_volume
    if label_stat_volume is not None:
        params["label_stat_volume"] = label_stat_volume
    if stat_threshold is not None:
        params["stat_threshold"] = stat_threshold
    if offset is not None:
        params["offset"] = offset
    if defects is not None:
        params["defects"] = defects
    return params


def mri_label2vol_cargs(
    params: MriLabel2volParameters,
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
    cargs.append("mri_label2vol")
    if params.get("labels") is not None:
        cargs.extend([
            "--label",
            *params.get("labels")
        ])
    if params.get("annotation") is not None:
        cargs.extend([
            "--annot",
            execution.input_file(params.get("annotation"))
        ])
    if params.get("segmentation") is not None:
        cargs.extend([
            "--seg",
            execution.input_file(params.get("segmentation"))
        ])
    cargs.extend([
        "--temp",
        execution.input_file(params.get("template"))
    ])
    if params.get("registration") is not None:
        cargs.extend([
            "--reg",
            execution.input_file(params.get("registration"))
        ])
    if params.get("identity_flag"):
        cargs.append("--identity")
    if params.get("fill_threshold") is not None:
        cargs.extend([
            "--fillthresh",
            str(params.get("fill_threshold"))
        ])
    if params.get("label_vox_vol") is not None:
        cargs.extend([
            "--labvoxvol",
            str(params.get("label_vox_vol"))
        ])
    if params.get("projection") is not None:
        cargs.extend([
            "--proj",
            params.get("projection")
        ])
    if params.get("subject") is not None:
        cargs.extend([
            "--subject",
            params.get("subject")
        ])
    if params.get("hemisphere") is not None:
        cargs.extend([
            "--hemi",
            params.get("hemisphere")
        ])
    cargs.extend([
        "--o",
        params.get("output_volume")
    ])
    if params.get("hits_volume") is not None:
        cargs.extend([
            "--hits",
            params.get("hits_volume")
        ])
    if params.get("label_stat_volume") is not None:
        cargs.extend([
            "--label-stat",
            params.get("label_stat_volume")
        ])
    if params.get("stat_threshold") is not None:
        cargs.extend([
            "--stat-thresh",
            str(params.get("stat_threshold"))
        ])
    if params.get("offset") is not None:
        cargs.extend([
            "--offset",
            str(params.get("offset"))
        ])
    if params.get("defects") is not None:
        cargs.extend([
            "--defects",
            params.get("defects")
        ])
    if params.get("native_vox2ras_flag"):
        cargs.append("--native-vox2ras")
    return cargs


def mri_label2vol_outputs(
    params: MriLabel2volParameters,
    execution: Execution,
) -> MriLabel2volOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriLabel2volOutputs(
        root=execution.output_file("."),
        output_vol=execution.output_file(params.get("output_volume")),
        hits_vol=execution.output_file(params.get("hits_volume")) if (params.get("hits_volume") is not None) else None,
        label_stat_vol=execution.output_file(params.get("label_stat_volume")) if (params.get("label_stat_volume") is not None) else None,
    )
    return ret


def mri_label2vol_execute(
    params: MriLabel2volParameters,
    execution: Execution,
) -> MriLabel2volOutputs:
    """
    Converts a label or a set of labels into a volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriLabel2volOutputs`).
    """
    params = execution.params(params)
    cargs = mri_label2vol_cargs(params, execution)
    ret = mri_label2vol_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_label2vol(
    template: InputPathType,
    output_volume: str,
    labels: list[str] | None = None,
    annotation: InputPathType | None = None,
    segmentation: InputPathType | None = None,
    registration: InputPathType | None = None,
    identity_flag: bool = False,
    fill_threshold: float | None = None,
    label_vox_vol: float | None = None,
    projection: str | None = None,
    subject: str | None = None,
    hemisphere: str | None = None,
    hits_volume: str | None = None,
    label_stat_volume: str | None = None,
    stat_threshold: float | None = None,
    offset: float | None = None,
    defects: str | None = None,
    native_vox2ras_flag: bool = False,
    runner: Runner | None = None,
) -> MriLabel2volOutputs:
    """
    Converts a label or a set of labels into a volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        template: Template volume; the output will have the same size and\
            geometry.
        output_volume: Output volume in which each voxel will have the number\
            of the label to which it is assigned.
        labels: Enter the name of the label file. For multiple labels, use\
            multiple --label flags.
        annotation: Surface annotation file. Use this to input annotations\
            directly.
        segmentation: Path to input segmentation.
        registration: tkregister-style registration matrix mapping LabelXYZ to\
            VolXYZ.
        identity_flag: Use the identity matrix as the registration.
        fill_threshold: Threshold for voxel fill; a value between 0 and 1.
        label_vox_vol: Volume of each label point; default is 1mm³.
        projection: Project the label along the surface normal. Type can be abs\
            or frac.
        subject: FREESURFER subject identifier; needed with --proj.
        hemisphere: Hemisphere to use for --proj or --annot. Legal values are\
            lh and rh.
        hits_volume: Hit volume, a multi-frame volume with one frame per label\
            showing the number of hits per voxel.
        label_stat_volume: Map the label stats field into the volume.
        stat_threshold: Only use label point where stat > thresh.
        offset: Add offset to the segmentation numbers.
        defects: Creates a segmentation volume of the surface defects.
        native_vox2ras_flag: Use native voxel-to-RAS transform instead of\
            tkregister-style.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriLabel2volOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_LABEL2VOL_METADATA)
    params = mri_label2vol_params(
        labels=labels,
        annotation=annotation,
        segmentation=segmentation,
        template=template,
        registration=registration,
        identity_flag=identity_flag,
        fill_threshold=fill_threshold,
        label_vox_vol=label_vox_vol,
        projection=projection,
        subject=subject,
        hemisphere=hemisphere,
        output_volume=output_volume,
        hits_volume=hits_volume,
        label_stat_volume=label_stat_volume,
        stat_threshold=stat_threshold,
        offset=offset,
        defects=defects,
        native_vox2ras_flag=native_vox2ras_flag,
    )
    return mri_label2vol_execute(params, execution)


__all__ = [
    "MRI_LABEL2VOL_METADATA",
    "MriLabel2volOutputs",
    "MriLabel2volParameters",
    "mri_label2vol",
    "mri_label2vol_params",
]
