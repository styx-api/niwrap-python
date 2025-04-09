# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MAKE_AVERAGE_SURFACE_METADATA = Metadata(
    id="9afad673a77a680068222efbae2c9b8e26d54dc3.boutiques",
    name="make_average_surface",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MakeAverageSurfaceParameters = typing.TypedDict('MakeAverageSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["make_average_surface"],
    "subjects": list[str],
    "fsgd_file": typing.NotRequired[InputPathType | None],
    "average_subject_name": typing.NotRequired[str | None],
    "subjects_dir": typing.NotRequired[str | None],
    "sd_out_dir": typing.NotRequired[str | None],
    "transform_file": typing.NotRequired[str | None],
    "icosahedron_number": typing.NotRequired[float | None],
    "surf_reg": typing.NotRequired[str | None],
    "left_hemi": bool,
    "right_hemi": bool,
    "force": bool,
    "annot_template": bool,
    "template_only": bool,
    "no_template_only": bool,
    "no_annot": bool,
    "no_cortex_label": bool,
    "annot_list": typing.NotRequired[list[str] | None],
    "meas_list": typing.NotRequired[list[str] | None],
    "no_surf2surf": bool,
    "no_symlink": bool,
    "version": bool,
    "echo": bool,
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
        "make_average_surface": make_average_surface_cargs,
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


class MakeAverageSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_average_surface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def make_average_surface_params(
    subjects: list[str],
    fsgd_file: InputPathType | None = None,
    average_subject_name: str | None = "average",
    subjects_dir: str | None = None,
    sd_out_dir: str | None = None,
    transform_file: str | None = None,
    icosahedron_number: float | None = 7,
    surf_reg: str | None = None,
    left_hemi: bool = False,
    right_hemi: bool = False,
    force: bool = False,
    annot_template: bool = False,
    template_only: bool = False,
    no_template_only: bool = False,
    no_annot: bool = False,
    no_cortex_label: bool = False,
    annot_list: list[str] | None = None,
    meas_list: list[str] | None = None,
    no_surf2surf: bool = False,
    no_symlink: bool = False,
    version: bool = False,
    echo: bool = False,
) -> MakeAverageSurfaceParameters:
    """
    Build parameters.
    
    Args:
        subjects: List of subject names.
        fsgd_file: File from which to get the subject list.
        average_subject_name: Average subject name.
        subjects_dir: Directory for SUBJECTS_DIR (if different from the\
            environment variable).
        sd_out_dir: Directory to put output data.
        transform_file: Filename of the transform file.
        icosahedron_number: Specify icosahedron number.
        surf_reg: Alternative registration surface name.
        left_hemi: Only process the left hemisphere.
        right_hemi: Only process the right hemisphere.
        force: Overwrite existing average subject data.
        annot_template: Use annotation when making tif.
        template_only: Useful when creating iterative atlases.
        no_template_only: Turns off --template-only.
        no_annot: Do not create average annotations.
        no_cortex_label: Do not create ?h.cortex.label.
        annot_list: List of annotations to use.
        meas_list: List of measurements to use.
        no_surf2surf: Use old parametric surface method.
        no_symlink: Do not use symbolic links, just copy files.
        version: Script version information.
        echo: Enable command echo for debugging.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "make_average_surface",
        "subjects": subjects,
        "left_hemi": left_hemi,
        "right_hemi": right_hemi,
        "force": force,
        "annot_template": annot_template,
        "template_only": template_only,
        "no_template_only": no_template_only,
        "no_annot": no_annot,
        "no_cortex_label": no_cortex_label,
        "no_surf2surf": no_surf2surf,
        "no_symlink": no_symlink,
        "version": version,
        "echo": echo,
    }
    if fsgd_file is not None:
        params["fsgd_file"] = fsgd_file
    if average_subject_name is not None:
        params["average_subject_name"] = average_subject_name
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if sd_out_dir is not None:
        params["sd_out_dir"] = sd_out_dir
    if transform_file is not None:
        params["transform_file"] = transform_file
    if icosahedron_number is not None:
        params["icosahedron_number"] = icosahedron_number
    if surf_reg is not None:
        params["surf_reg"] = surf_reg
    if annot_list is not None:
        params["annot_list"] = annot_list
    if meas_list is not None:
        params["meas_list"] = meas_list
    return params


def make_average_surface_cargs(
    params: MakeAverageSurfaceParameters,
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
    cargs.append("make_average_surface")
    cargs.extend(params.get("subjects"))
    if params.get("fsgd_file") is not None:
        cargs.extend([
            "--fsgd",
            execution.input_file(params.get("fsgd_file"))
        ])
    if params.get("average_subject_name") is not None:
        cargs.extend([
            "--out",
            params.get("average_subject_name")
        ])
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sdir",
            params.get("subjects_dir")
        ])
    if params.get("sd_out_dir") is not None:
        cargs.extend([
            "--sd-out",
            params.get("sd_out_dir")
        ])
    if params.get("transform_file") is not None:
        cargs.extend([
            "--xform",
            params.get("transform_file")
        ])
    if params.get("icosahedron_number") is not None:
        cargs.extend([
            "--ico",
            str(params.get("icosahedron_number"))
        ])
    if params.get("surf_reg") is not None:
        cargs.extend([
            "--surf-reg",
            params.get("surf_reg")
        ])
    if params.get("left_hemi"):
        cargs.append("--lh")
    if params.get("right_hemi"):
        cargs.append("--rh")
    if params.get("force"):
        cargs.append("--force")
    if params.get("annot_template"):
        cargs.append("--annot-template")
    if params.get("template_only"):
        cargs.append("--template-only")
    if params.get("no_template_only"):
        cargs.append("--no-template-only")
    if params.get("no_annot"):
        cargs.append("--no-annot")
    if params.get("no_cortex_label"):
        cargs.append("--no-cortex-label")
    if params.get("annot_list") is not None:
        cargs.extend([
            "--annot",
            *params.get("annot_list")
        ])
    if params.get("meas_list") is not None:
        cargs.extend([
            "--meas",
            *params.get("meas_list")
        ])
    if params.get("no_surf2surf"):
        cargs.append("--no-surf2surf")
    if params.get("no_symlink"):
        cargs.append("--no-symlink")
    if params.get("version"):
        cargs.append("--version")
    if params.get("echo"):
        cargs.append("--echo")
    return cargs


def make_average_surface_outputs(
    params: MakeAverageSurfaceParameters,
    execution: Execution,
) -> MakeAverageSurfaceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MakeAverageSurfaceOutputs(
        root=execution.output_file("."),
    )
    return ret


def make_average_surface_execute(
    params: MakeAverageSurfaceParameters,
    execution: Execution,
) -> MakeAverageSurfaceOutputs:
    """
    Creates average surfaces and curvatures from a set of subjects.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MakeAverageSurfaceOutputs`).
    """
    params = execution.params(params)
    cargs = make_average_surface_cargs(params, execution)
    ret = make_average_surface_outputs(params, execution)
    execution.run(cargs)
    return ret


def make_average_surface(
    subjects: list[str],
    fsgd_file: InputPathType | None = None,
    average_subject_name: str | None = "average",
    subjects_dir: str | None = None,
    sd_out_dir: str | None = None,
    transform_file: str | None = None,
    icosahedron_number: float | None = 7,
    surf_reg: str | None = None,
    left_hemi: bool = False,
    right_hemi: bool = False,
    force: bool = False,
    annot_template: bool = False,
    template_only: bool = False,
    no_template_only: bool = False,
    no_annot: bool = False,
    no_cortex_label: bool = False,
    annot_list: list[str] | None = None,
    meas_list: list[str] | None = None,
    no_surf2surf: bool = False,
    no_symlink: bool = False,
    version: bool = False,
    echo: bool = False,
    runner: Runner | None = None,
) -> MakeAverageSurfaceOutputs:
    """
    Creates average surfaces and curvatures from a set of subjects.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects: List of subject names.
        fsgd_file: File from which to get the subject list.
        average_subject_name: Average subject name.
        subjects_dir: Directory for SUBJECTS_DIR (if different from the\
            environment variable).
        sd_out_dir: Directory to put output data.
        transform_file: Filename of the transform file.
        icosahedron_number: Specify icosahedron number.
        surf_reg: Alternative registration surface name.
        left_hemi: Only process the left hemisphere.
        right_hemi: Only process the right hemisphere.
        force: Overwrite existing average subject data.
        annot_template: Use annotation when making tif.
        template_only: Useful when creating iterative atlases.
        no_template_only: Turns off --template-only.
        no_annot: Do not create average annotations.
        no_cortex_label: Do not create ?h.cortex.label.
        annot_list: List of annotations to use.
        meas_list: List of measurements to use.
        no_surf2surf: Use old parametric surface method.
        no_symlink: Do not use symbolic links, just copy files.
        version: Script version information.
        echo: Enable command echo for debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeAverageSurfaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_AVERAGE_SURFACE_METADATA)
    params = make_average_surface_params(
        subjects=subjects,
        fsgd_file=fsgd_file,
        average_subject_name=average_subject_name,
        subjects_dir=subjects_dir,
        sd_out_dir=sd_out_dir,
        transform_file=transform_file,
        icosahedron_number=icosahedron_number,
        surf_reg=surf_reg,
        left_hemi=left_hemi,
        right_hemi=right_hemi,
        force=force,
        annot_template=annot_template,
        template_only=template_only,
        no_template_only=no_template_only,
        no_annot=no_annot,
        no_cortex_label=no_cortex_label,
        annot_list=annot_list,
        meas_list=meas_list,
        no_surf2surf=no_surf2surf,
        no_symlink=no_symlink,
        version=version,
        echo=echo,
    )
    return make_average_surface_execute(params, execution)


__all__ = [
    "MAKE_AVERAGE_SURFACE_METADATA",
    "MakeAverageSurfaceOutputs",
    "MakeAverageSurfaceParameters",
    "make_average_surface",
    "make_average_surface_params",
]
